import pytest
import Student
import System


def test_check_ontime(grading_system):
    username = "akend3"
    password = "123454321"
    due_date = "2/1/20"

    grading_system.login(username, password)
    assert grading_system.usr.check_ontime('2/2/20', due_date) == False
    assert grading_system.usr.check_ontime('1/1/20', due_date) == True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem