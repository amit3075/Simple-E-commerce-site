from django.http import HttpResponse
from django.shortcuts import render



def aboutus(request):
    return HttpResponse("welcome to Budhha food land")

def Product(request):
    return HttpResponse("hello")
def course(request):
    return HttpResponse("welcome courses")
def courseDetail(request,courseid):
    return HttpResponse(courseid)

def homepage(reuest):
    return render(request,"index.html")
