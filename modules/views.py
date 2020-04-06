from django.shortcuts import render
from .models import Course
from .models import Module
from .models import Task

# Create your views here.

def moduleList(request):
    # Get all modules from database
    queryset = Module.objects.all()
    
    # Create course dict with modules
    courses = {}
    for module in queryset:
        if module.course not in courses:
            courses[module.course] = []
        courses[module.course].append(module)
    
    context = {
        "courses":courses
    }
    return render(request,"moduleList.html",context)
