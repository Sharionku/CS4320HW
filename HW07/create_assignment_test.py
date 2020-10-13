import pytest
import System
import Staff

def test_create_assignment(grading_system):
   username = "cmhbf5"
   password ="bestTA"
   grading_system.login(username, password)
   grading_system.usr.create_assignment('assignment3', '3/5/20', 'databases')
   assert grading_system.courses['databases']['assignments']['assignment3']['due_date'] == '3/5/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
