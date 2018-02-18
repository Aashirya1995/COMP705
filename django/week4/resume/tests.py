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
        my_education = None
        #my_education.save()
        my_experience = None
        #my_experience.save()

    def test_last_name_first_name(self):
        '''
        Test case for get_last_name_first_name
        '''
        r = Resume.objects.first()
        self.assertEqual(r.get_last_name_first_name(), "Kaushik, Aashirya")

    def test_full_name(self):
        '''
        Test case for get_full_name method
        '''
        r = Resume.objects.first()
        self.assertEqual(r.get_full_name(), "Aashirya, Kaushik")

    def test_education(self):
        '''
        Test case for get_education
        '''
        r = Resume.objects.first()
        actual = list(r.get_education())
        expected = list(r.education_set.all())
        self.assertEqual(actual,expected)

    def test_experience(self):
        '''
        Test case for get_experience
        '''
        r = Resume.objects.first()
        actual = list(r.get_experience())
        expected = list(r.experience_set.all())
        self.assertEqual(actual,expected)
