from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMin, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index (request):
    return render(request, 'clubApp/index.html')

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'clubApp/meetings.html', {'meeting_list' : meeting_list})

def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'clubApp/meeting_detail.html', {'meeting' : meeting})

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'clubApp/resources.html', {'resource_list' : resource_list})