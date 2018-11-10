from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
  # the index function is called when root is visited
# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)

def test(request):
  response = "I am test olleH"
  return HttpResponse(response)

def index(request):
  response = "Placeholder to later display all the list of blogs"
  return HttpResponse(response)

def new(request):
  response = "Placeholder to display a new form to create a new blog"
  return HttpResponse(response)
  
def create(request):
  return redirect("/")

def show(request, show_number):
  response = "Placeholder to display blog " + show_number
  return HttpResponse(response)

def edit(request, show_number):
  response = "Placeholder to display a form to edit blog #" + show_number
  return HttpResponse(response)

def destroy(request, show_number):
  print ("redirecting to root")
  return redirect("/")
# Create your views here.
