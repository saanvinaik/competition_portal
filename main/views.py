from django.shortcuts import render
from .models import Branch, Category
# Create your views here.

#home page

def home(request):
    return render(request , 'index.html')

#category
def category_list(request):
    data_cat = Category.objects.all().order_by('-id')
    return render(request , 'category_list.html' , {'data_cat':data_cat})

def branch_list(request):
    data_branch = Branch.objects.all().order_by('-id')
    return render(request , 'branch_list.html' , {'data_branch':data_branch})



#branch

