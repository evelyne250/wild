from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request, 'gallery.html')