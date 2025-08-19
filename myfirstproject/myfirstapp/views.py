from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a + b)

def intro (request,name,age):
    mydictionary = {
        "name" : name,
        "age" : age
    }
    return JsonResponse(mydictionary)

def myfirstpage(request):
    return render(request,'index.html')

def mysecondpage(request):
    return render(request,'second.html')

def mythirdpage(request):
    var = 'hello there'
    greeting = 'How are You!!'
    fruits = ['apple','banana','litchi','mango']
    mydictionary = {
        "var" : var,
        "Greetings":greeting,
        "myfruits":fruits
    }
    return render(request,'third.html',context=mydictionary)

def myimagepage(request):
    return render(request,'imagepage.html')

def myimagepage2(request):
    return render(request,'imagepage2.html')

def myimagepage3(request):
    return render(request,'imagepage3.html')

def myimagepage4(request):
    return render(request,'imagepage4.html')