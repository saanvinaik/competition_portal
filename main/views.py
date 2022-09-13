from django.shortcuts import render
from .models import slider,Branch, Category , Competition
# Create your views here.

#home page

def home(request):
    sliders = slider.objects.all().order_by('-id')
    data = Competition.objects.filter(is_featured = True).order_by('-id')
    return render(request , 'index.html' , {'data':data , 'sliders':sliders})

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
    cats = Competition.objects.distinct().values('category__title','category__id')
    branchs = Competition.objects.distinct().values('branch__title','branch_id')
    years = Competition.objects.distinct().values('year__title','year__id')
    domains = Competition.objects.distinct().values('domain__title','domain__id')
    return render(request , 'competition_list.html' ,
    {
        'data_competition':data_competition,
        'cats':cats,
        'branchs':branchs,
        'years':years,
        'domains':domains

    }
    )


