from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Courses

def index(request):
    return render(request, 'index.html', {"courses": Courses.objects.all()})

def add_course(request):
    # if request.method != request.POST:
    #     return redirect('/')
    errors = Courses.objects.validate_user(request.POST)

    if len(errors):
		for tag, error in errors.iteritems():
    			messages.error(request, error)
		return redirect('/')
    
    name = request.POST['name']
    description= request.POST['description']
    Courses.objects.create(name=name, description=description)

    return redirect('/')

def delete(request, id):
    course = Courses.objects.get(id=id)
    course.delete()
    return redirect('/')

def clear(request):
    return redirect('/')

def results(request, id):
    result = Courses.objects.get(id=id)
    course = {
        'course': result
    }
    return render(request, 'results.html', course)
