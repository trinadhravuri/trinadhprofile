from django.shortcuts import render,redirect
from .models import Enquiry,Skills,Projects
from .forms import EnquiryForm
# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    skills = Skills.objects.all()
    skills = skills[:4]
    projects = Projects.objects.all()
    projects = projects[:4]
    form = EnquiryForm
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'skills':skills,
        'projects':projects,
        'form':form
    }
    return render(request,'myprofile/home.html',context)

def allskills(request):
    skills = Skills.objects.all()
    context = {
        'skills':skills
    }
    return render(request,'myprofile/allskills.html',context)

def allprojects(request):
    projects = Projects.objects.all()
    context = {
        'projects':projects
    }
    return render(request,'myprofile/allprojects.html',context)

def singleskill(request,pk):
    skill = Skills.objects.get(pk=pk)
    context={
        'skill':skill
    }
    return render(request,'myprofile/singleskill.html',context)