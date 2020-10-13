import pytest
import System

def test_drop_stu(grading_system):

    username = "goggins"
    password = "augurrox"
    grading_system.login(username, password)

    grading_system.usr.drop_student("akend3", "databases")
    grading_system.reload_data
    # assert grading_system.users["akend3"] != "akend3"
    assert 'databases' not in grading_system.users['akend3']['courses']


@pytest.fixture
def grading_system():
        gradingSystem = System.System()
        gradingSystem.load_data()
        return gradingSystem