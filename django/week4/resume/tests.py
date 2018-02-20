from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTestCase(TestCase):
    """
    Test cases for the Models and the new methods
    """
    def setUp(self):

        self.my_resume = Resume.objects.create(first_name = 'Aashirya', last_name = 'Kaushik')
        #my_resume.save()
        self.my_education = Education.objects.create(parent_resume = self.my_resume, instituition_name =  "UNH", location = "Manchester",
                               degree =  "Bachelors", major = "Computer Science", gpa = "3.73" )

        self.my_experience = Experience.objects.create(parent_resume = self.my_resume, title =  "Dean's Assistant", location = "Dean's Office, UNHM",
                                start_date =  "2016-06-05", end_date = "2016-08-04", description = "Maintained the Dean’s and Associate Dean’s calendar." )




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
        self.assertEqual(actual_edu,expected_edu) # checks if actual is equal to expected.

    def test_experience(self):
        '''
        Test case for get_experience
        '''
        exp = Resume.objects.first() # gets the first object from the Resume class
        actual_exp = list(exp.get_experience())
        expected_exp = list(exp.experience_set.all())
        self.assertEqual(actual_exp,expected_exp) # checks if actual is equal to expected.
