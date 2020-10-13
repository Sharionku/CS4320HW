import pytest
import System
import Student


def test_view_assignments_due(grading_system):
    username = "akend3"
    password = "123454321"
    
    grading_system.login(username, password)
    # Test if the due date is correct
    assert '2/8/20' in grading_system.usr.view_assignments('comp_sci')[1]

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem