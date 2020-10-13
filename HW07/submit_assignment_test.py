import pytest
import System

def test_submit_assignment(grading_system):
    
    username = "akend3"
    password = "123454321"
    course = "comp_sci"
    assignment = "assignment1"
    submission_date = "2/1/20"
    submission = "Blah Blah Blah"

    grading_system.login(username, password)
    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    assert assignment in grading_system.users[username]['courses'][course]
    assert grading_system.users[username]['courses'][course][assignment]['submission_date'] == submission_date
    assert grading_system.users[username]['courses'][course][assignment]['submission'] == submission
   

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem