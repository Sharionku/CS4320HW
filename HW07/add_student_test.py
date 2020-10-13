import pytest
import Professor
import System

def test_add_student(grading_system):
    username = "goggins"
    password ="augurrox"
    grading_system.login(username, password)
    grading_system.usr.add_student('akend3', 'software_engineering')
    assert 'software_engineering' in grading_system.users['akend3']['courses']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem