""" Assessments, trainees, quiz and questions with inheritance """
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


# pylint: disable=too-few-public-methods
class Question:
    """ Question contains question, chosen answer and correct answer """

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer


# pylint: disable=too-few-public-methods
class Quiz:
    """ Quiz contains questions, name and type of assessment """

    def __init__(self, questions: list, name: str, quiz_type: str):
        self.questions = questions
        self.name = name
        self.quiz_type = quiz_type


class Marking:
    """ Marking to calculate score for assessment"""

    def __init__(self, quiz: Quiz):
        self._quiz = quiz

    def mark(self) -> int:
        """ Return the total score for the assessment as a percentage,
        rounded to zero decimal places """

        questions_list = self._quiz.questions
        if not questions_list:
            return 0

        score = 0
        for question in questions_list:
            if question.chosen_answer == question.correct_answer:
                score += 1

        total_score = int((score / len(questions_list)) * 100)

        return total_score

    def generate_assessment(self) -> Assessment:
        """Return instance of correct subclass of Assessment, correct name and score"""
        assessment_type = self._quiz.quiz_type
        if assessment_type == "multiple-choice":
            assessment = MultipleChoiceAssessment(self._quiz.name, self.mark())
        elif assessment_type == "technical":
            assessment = TechnicalAssessment(self._quiz.name, self.mark())
        elif assessment_type == "presentation":
            assessment = TechnicalAssessment(self._quiz.name, self.mark())
        return assessment


# if __name__ == "__main__":
#     # Example questions and quiz
#     questions = [
#         Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
#         Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
#         Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
#         Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
#         Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
#     ]
#     quiz = Quiz(questions, "Maths Quiz", "multiple-choice")
#     marking = Marking(quiz)
#     print(marking.mark())

# Add an implementation for the Marking class below to test your code
