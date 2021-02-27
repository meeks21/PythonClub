from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMin, Resource, Event
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm

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

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'clubApp/newmeeting.html',{'form': form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'clubApp/newresource.html',{'form':form})

    