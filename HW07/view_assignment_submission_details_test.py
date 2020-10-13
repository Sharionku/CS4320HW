import pytest
import System

def test_assignment_submission_details(grading_system):
    
    username = "akend3"
    password = "123454321"
    course = "comp_sci"
    assignment = "assignment1"
    submission = "Blah Blah Blah"

    grading_system.login(username, password)
    assert grading_system.users[username]['courses'][course][assignment]['submission'] == submission
   

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem