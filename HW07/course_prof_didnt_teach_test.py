import pytest
import System
import Staff
import Professor
#test professor cannot check the grade for class he/she didn't teach
def test_course_prof_didnt_teach(grading_system):

   grading_system.login('goggins', 'augurrox')
   grades = grading_system.usr.check_grades('akend3','comp_sci')
   assert 'goggins' in grading_system.courses['comp_sci']['professor']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem