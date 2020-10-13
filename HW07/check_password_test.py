import pytest
import System

def test_check_password(grading_system):
    username = 'akend3'
    assert grading_system.check_password(username,'123454321')==True
    assert grading_system.check_password(username, '0987433')==False
    assert grading_system.check_password(username, 'boomr345')==False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem