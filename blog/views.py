from django.shortcuts import render

# Create your views here.
from .models import BlogPage
from .models import BlogCategory
from .models import BlogTagIndexPage

def blogpage(request):
    posts=BlogPage.objects.all()
    category=BlogCategory.objects.all()
    return render(request,'blog/blog_index_page.html',{'posts':posts,'categori':category})

def category_dao(request,category_id):
    category=BlogCategory.objects.get(pk=category_id)
    categories=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    return render(request,'blog/category.html',{'single_category':category,'categori':categories,'posts':posts})
