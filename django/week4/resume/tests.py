from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTestCase(TestCase):
    """
    Test cases for the Models and the new methods
    """
    def setUp(self):

        my_resume = Resume(first_name = 'Aashirya', last_name = 'Kaushik')
        my_resume.save()

    def test_last_name_first_name(self):
        '''
        Test case for get_last_name_first_name
        '''
        l_name = Resume.objects.first() #gets the first object from the Resume class.
        self.assertEqual(l_name.get_last_name_first_name(), "Kaushik, Aashirya") # Checks if l_name.get_last_name_first_name is equal to the string.

    def test_full_name(self):
        '''
        Test case for get_full_name method
        '''
        f_name = Resume.objects.first()  # gets the first object from the Resume class.
        self.assertEqual(f_name.get_full_name(), "Aashirya, Kaushik") # checks if f_name.get_full_name is equal to the string.

    def test_education(self):
        '''
        Test case for get_education
        '''
        edu = Resume.objects.first() # gets the first object from the Resume class.
        actual_edu = list(edu.get_education())
        expected_edu = list(edu.education_set.all())
        self.assertEqual(actual,expected) # checks if actual is equal to expected.

    def test_experience(self):
        '''
        Test case for get_experience
        '''
        exp = Resume.objects.first() # gets the first object from the Resume class
        actual_exp = list(exp.get_experience())
        expected_exp = list(exp.experience_set.all())
        self.assertEqual(actual,expected) # checks if actual is equal to expected.
