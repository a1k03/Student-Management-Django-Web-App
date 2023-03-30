from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse 
from django.core.mail import send_mail
from django.conf import settings
from .models import Student
from .forms import StudentForm

# Create your views here.

def index(request):  # this argument will represent the http request that the user made to access the web server
     return render(request, 'students/index.html', {
          'students': Student.objects.all()
     })

def contact(request):

	if request.method == 'POST':
		message = request.POST['message']

		send_mail('Contact Form',
		 message, 
		 settings.EMAIL_HOST_USER,
		 ['amir.khan.sch"gmail.com'], 
		 fail_silently=False)
	return render(request, 'students/contact.html')

def see_student(request, id):
     student = Student.objects.get(pk=id) # get the student whose primary key in the db is equal to the id passed as an argument
     return HttpResponseRedirect(reverse('index'))  # redirects back to the index route

def add(request):
     if request.method == 'POST':
          form = StudentForm(request.POST)
          if form.is_valid():
               new_student_number = form.cleaned_data['student_num']
               new_first_name = form.cleaned_data['first_name']
               new_last_name = form.cleaned_data['last_name']
               new_email = form.cleaned_data['email']
               new_course = form.cleaned_data['course']

               new_student = Student(
                    student_num = new_student_number,
                    first_name = new_first_name,
                    last_name = new_last_name,
                    email = new_email,
                    course = new_course
               )
               new_student.save()
               return render(request, 'students/add.html', {
                    'form': StudentForm(),
                    'success': True
               })
     else:
          form = StudentForm()
     return render(request, 'students/add.html', {
          'form': StudentForm()
     })

def edit(request, id):
     if request.method == 'POST':
          student = Student.objects.get(pk=id)
          form = StudentForm(request.POST, instance=student)
          if form.is_valid():
               form.save()
               return render(request, 'students/edit.html', {
                    'form': form,
                    'success': True
               })
     else:
          student = Student.objects.get(pk=id)
          form = StudentForm(instance=student)
          return render(request, 'students/edit.html', {
               'form': form
          })

def delete(request, id):
  if request.method == 'POST':
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))