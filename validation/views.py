from django.shortcuts import render
from django.http import HttpResponse
from .models import Admission

# Create your views here.

def home(request):
    context={}
    admissions = Admission.objects.all()
    context['admissions'] = admissions
    
    return  render(request,'validation/index.html',context)