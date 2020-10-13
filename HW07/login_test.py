import pytest
import System
import json

def test_login(grading_system):
    username = 'goggins'
    password = 'augurrox'
    grading_system.login(username,password)
    assert grading_system.users[username]['role'] == 'professor'
    assert grading_system.users[username]['password'] == 'augurrox'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem