import pytest
import System


def test_view_assignments(grading_system):
    username = "akend3"
    password = "123454321"

    grading_system.login(username, password)
    assert grading_system.usr.view_assignments('comp_sci')[1]==['assignment2','2/8/20']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem