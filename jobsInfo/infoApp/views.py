from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def hydjobsinfo(request):
    date= datetime.datetime.now()
    msg="<h1>This is Hyderabad job information </h1>"
    msg +="<h2>Date and Time of the job" + str(date) + "</h2>"
    return HttpResponse(msg)

def mumbaijobsinfo(request):
    date= datetime.datetime.now()
    msg="<h1>This is Mumbai job information </h1>"
    msg +="<h2>Date and Time of the job" + str(date) + "</h2>"
    return HttpResponse(msg)

def punejobsinfo(request):
    date= datetime.datetime.now()
    msg="<h1>This is Pune job information </h1>"
    msg +="<h2>Date and Time of the job" + str(date) + "</h2>"
    return HttpResponse(msg)