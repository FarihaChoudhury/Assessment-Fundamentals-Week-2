from datetime import date, datetime

# You should have a `Trainee` class that has the following attributes:

# - `name` - str
# - `email` - str
# - `date_of_birth` - `date` object
# - `assessments` - list[Assessment]

# It has methods to:

# - `get_age() -> int` - returns the age of the trainee in years
# - `add_assessment(assessment: Assessment) -> None` - adds an `Assessment` to the trainee's list of assessments
# - `get_assessment(name: str) -> Assessment | None` - returns the `Assessment` object that has the name given
#   - Return `None` if not found

# You should have an `Assessment` class that has the following attributes:

# - `name` - str
# - `type` - str
#   - Can only be `multiple-choice`, `technical` or `presentation`. Throw a ValueError if not.
# - score - float (0-100). Throw a ValueError if outside of this range.


class Assessment:
    def __init__(self, name: str, type: str, score: float):
        self.name = name
        self.validate_type(type)
        self.validate_score(score)
        self.type = type
        self.score = score

    def validate_type(self, type):
        if type != "multiple-choice" and type != "technical" and type != "presentation":
            raise ValueError("Invalid type of assessment")

    def validate_score(self, score):
        if score > 100 or score < 0:
            raise ValueError("Outside range")


class Trainee:
    def __init__(self, name: str, email: str, date_of_birth: date):
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        today = date.today()
        age = today.year - self.date_of_birth.year - \
            (((today.month, today.day) <
             (self.date_of_birth.month, self.date_of_birth.day)))
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
