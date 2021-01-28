from django.shortcuts import render, redirect
from django.http import HttpResponse


#Home Page view
def home(request):

    return render(request, 'pages/home.html')