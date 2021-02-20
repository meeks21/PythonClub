from django.test import TestCase
from .models import Meeting, MeetingMin, Resource, Event


# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Intro to Python Club')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Intro to Python Club')

    def test_tablename(self): 
        self.assertEqual(str(Meeting._meta.db_table), 'meeting') 

class MeetingMinTest(TestCase):
    def setUp(self):
        self.type=MeetingMin(minutestext='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(MeetingMin._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.type=Event(eventtitle='This is a test')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'This is a test')

    def test_tablename(self): 
        self.assertEqual(str(Event._meta.db_table), 'event')