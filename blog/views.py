from django.shortcuts import render

# Create your views here.
from .models import BlogPage
from .models import BlogCategory
from .models import BlogTagIndexPage
def blogpage2(request):

    category=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    print(category)
    return render(request,'blogbase.html',{'categori':category,'posts':posts})

def blogpage(request):
    posts=BlogPage.objects.all()
    category=BlogCategory.objects.all()
    tagIndex=BlogTagIndexPage.objects.all()

    return render(request,'blog.html',{'posts':posts,'tags':tagIndex,'categori':category})

def category_dao(request,category_id):
    category=BlogCategory.objects.get(pk=category_id)
    categories=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    return render(request,'category.html',{'single_category':category,'categori':categories,'posts':posts})

def blogtag(request):
        posts=BlogPage.objects.all()
        category=BlogCategory.objects.all()
        tagIndex=BlogTagIndexPage.objects.all()

        return render(request,'blog.html',{'posts':posts,'tags':tagIndex,'categori':category})
