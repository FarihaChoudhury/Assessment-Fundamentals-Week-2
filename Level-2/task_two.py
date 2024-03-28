""" Assessments and trainees with inheritance"""
from datetime import date
from abc import ABC, abstractmethod


class Assessment(ABC):
    """ Different assessments, their names, types, and score"""

    def __init__(self, name: str, score: float):
        self.name = name
        self.validate_score(score)
        self.score = score

    def validate_type(self, assessment_type):
        """ Validates if assessment if of correct type """
        if assessment_type not in ('multiple-choice', 'technical', 'presentation'):
            raise ValueError("Invalid type of assessment")

    def validate_score(self, score):
        """ Validates if assessment score is within correct range """
        if score > 100 or score < 0:
            raise ValueError("Outside range")

    @abstractmethod
    def calculate_score(self):
        """ Calculate score """
        # pylint: disable-next=unnecessary-pass
        pass


class MultipleChoiceAssessment(Assessment):
    """ Assessment type Multiple choice """

    def calculate_score(self):
        """ 70% weighting score """
        return self.score * 0.7


class TechnicalAssessment(Assessment):
    """ Assessment type Technical """

    def calculate_score(self):
        """ 100% weighting score """
        return self.score


class PresentationAssessment(Assessment):
    """ Assessment type Presentation """

    def calculate_score(self):
        """ 60% weighting score """
        return self.score * 0.6


class Trainee:
    """ Trainee with name, email, date of birth and assessments """

    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        """ Computes age of trainee """
        today = date.today()
        age = today.year - self.date_of_birth.year - \
            (((today.month, today.day) <
             (self.date_of_birth.month, self.date_of_birth.day)))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """ Adds assessments to trainee """
        self.validate_assessment(assessment)
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """ Retrieves assessment for trainee by assessment name"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def validate_assessment(self, assessment: Assessment) -> None:
        """ Validates if an assessment is of Assessment subclass type"""
        if not isinstance(assessment, (PresentationAssessment, TechnicalAssessment,
                                       MultipleChoiceAssessment)):
            raise TypeError("Incorrect assessment type")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
