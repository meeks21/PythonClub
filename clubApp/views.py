from django.shortcuts import render
from .models import Meeting, MeetingMin, Resource, Event
# Create your views here.
def index (request):
    return render(request, 'clubApp/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubApp/meetings.html', {'meeting_list' : meeting_list})

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubApp/resources.html', {'resource_list' : resource_list})