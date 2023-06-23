from django.shortcuts import render
from .models import Enquiry
# Create your views here.

def base(request):
    return render(request,'myprofile/base.html')
