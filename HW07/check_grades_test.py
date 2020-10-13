import pytest
import System
import Staff


def test_check_grade(grading_system):
    username = "akend3"
    password = "123454321"
    grade = 100

    grading_system.login(username, password)
    grades = grading_system.usr.check_grades('comp_sci')
    # correct grade should be 99
    assert grades[0][1] == grade


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem