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

    return render(request,'blog/blog_index_page.html',{'posts':posts,'tags':tagIndex,'categori':category})

def category_dao(request,category_id):
    category=BlogCategory.objects.get(pk=category_id)
    categories=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    return render(request,'blog/category.html',{'single_category':category,'categori':categories,'posts':posts})


def singlepage(request,post_id):
    post=BlogPage.objects.get(pk=post_id)
    categories=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    return render(request,'blog/blog_page.html',{'page':post,'categori':categories,'posts':posts})

def blog_tag_index_page(request):
    categories=BlogCategory.objects.all()
    return render(request,'blog/blog_tag_index_page.html',{'categori':categories})
