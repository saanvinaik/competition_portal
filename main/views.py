from django.shortcuts import render
from .models import Branch, Category , Competition
# Create your views here.

#home page

def home(request):
    return render(request , 'index.html')

#category
def category_list(request):
    data_cat = Category.objects.all().order_by('-id')
    return render(request , 'category_list.html' , {'data_cat':data_cat})

#brand
def branch_list(request):
    data_branch = Branch.objects.all().order_by('-id')
    return render(request , 'branch_list.html' , {'data_branch':data_branch})

def competition_list(request):
    data_competition = Competition.objects.all().order_by('-id')
    return render(request , 'competition_list.html' , {'data_competition':data_competition})


