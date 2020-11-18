from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Group

# Create your views here.
def index(request):
    Data = {'Groups': Group.objects.all()}
    return render(request,'pages/home.html', Data)