from django.test import TestCase
from .models import Meeting, MeetingMin, Resource, Event


# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingname='Intro to Python Club')
    
    def test_type(self):
        self.assertEqual(str(self.type), 'Intro to Python Club')