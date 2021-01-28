from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from teachers.models import Teachers, Subjects
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.contrib import messages
from .forms import TeachersModelForm

#all teachers
def teachers(request):
    teachers = Teachers.objects.all()
    subjects = Subjects.objects.all()

    subjects_taken = Subjects.objects.values_list()

    print(subjects_taken)

    context = {'teachers':teachers,'subjects':subjects, }

    return render(request, 'teachers/teachers.html', context)


def add_teacher(request):
    if request.method == 'POST':
        form = TeachersModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers:teachers')
    else:
        form = TeachersModelForm()
    return render(request,
                  'teachers/add_teacher.html',{
                      'form': form})

#single Teacher
def teacher(request, id):
    teacher = get_object_or_404(Teachers, pk=id)

    context = {'teacher':teacher,}

    return render(request, 'teachers/single.html', context)




def search(request):
    queryset_list = Teachers.objects.all()
    subjects = Subjects.objects.all()

    #last_name search
    if 'last_name' in request.GET:
        last_name = request.GET['last_name']
        if last_name:
            queryset_list = queryset_list.filter(last_name__icontains=last_name)
           
           
            
    #subject search
    if 'subjects' in request.GET:
        subjects = request.GET['subjects']
        if subjects:
            queryset_list = queryset_list.filter(subjects_taken__subject_name__icontains=subjects)
            
            
    context={
        'teachers':queryset_list,
        'subjects':subjects,
        'values':request.GET,

    }

    return render(request, 'teachers/search.html', context)