import pytest
import System

def test_number_of_assignment(grading_system):
    
    username = "akend3"
    password = "123454321"
    course = "comp_sci"
    submission = "Blah Blah Blah"
    number_of_assignments = 2

    grading_system.login(username, password)
   
   #test the number of assignments in a course
    assert len(grading_system.users[username]['courses'][course]) == number_of_assignments
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem