import pytest
import System

def test_wrong_password(grading_system):
    username = 'akend3'
    password = '1234321'

    # Test a wrong password and this should fail
    assert grading_system.check_password(username, password)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem