from django.test import TestCase
from .models import Meeting, MeetingMin, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.models import User
import datetime
from django.urls import reverse_lazy, reverse

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

class newMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
            'meetingtitle':'test',
            'meetingdate':'4-1-2021',
            'meetingtime':'6:00pm',
            'location':'SCC',
            'agenda':'test test',
            
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class newResourceForm(TestCase):
    def test_resourceform(self):
        data={
            'resourcename':'test',
            'resourcetype':'book',
            'URL':'https://www.test.com/',
            'dateentered':'4-1-2021',
            'userid':'kemar',
            'description':'test test',
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1',password='@Bopgun1988')

        self.type=Resource.objects.create(resourcename='Test',resourcetype='resource1', URL='http://www.test.com', dateentered=datetime.date(2021,1,10), userid=self.test_user, description="test test test")

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/clubApp/newresource/')
