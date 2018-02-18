from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.
class ResumeTestCase(TestCase):
    """
    """
    def setUp(self):

        my_resume = Resume(first_name = 'Aashirya', last_name = 'Kaushik')
        my_resume.save()
        my_education = None
        #my_education.save()
        my_experience = None
        #my_experience.save()

    def test_last_name_first_name(self):
        r = Resume.objects.first()
        self.assertEqual(r.get_last_name_first_name(), 'Kaushik Aashirya')

    def test_full_name(self):
        r = Resume.objects.first()
        self.assertEqual(r.get_full_name(), 'Aashirya Kaushik')

    def test_education(self):
        r = Resume.objects.first()
        actual = list(r.get_education())
        expected = list(r.education_set.all())
        self.assertEqual(actual,expected)

    def test_experience(self):
        r = Resume.objects.first()
        actual = list(r.get_experience())
        expected = list(r.experience_set.all())
        self.assertEqual(actual,expected)
