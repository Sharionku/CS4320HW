import pytest
import Staff
import System

def test_change_grade(grading_system):
    grading_system.login('goggins', 'augurrox')
    grading_system.usr.change_grade('hdjsr7', 'databases', 'assignment2', 99)
    assert grading_system.users['hdjsr7']['courses']['databases']['assignment2']['grade'] == 99



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem