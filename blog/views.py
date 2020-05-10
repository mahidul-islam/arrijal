from django.shortcuts import render

# Create your views here.
from .models import BlogPage
from .models import BlogCategory
from .models import BlogTagIndexPage
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

def blogpage(request):
    posts=BlogPage.objects.all()
    category=BlogCategory.objects.all()
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    paginator = Paginator(posts, 2)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,'blog/blog_index_page.html',{'posts':posts,'categori':category})

def category_dao(request,category_id):
    category=BlogCategory.objects.get(pk=category_id)
    categories=BlogCategory.objects.all()
    posts=BlogPage.objects.all()
    return render(request,'blog/category.html',{'single_category':category,'categori':categories,'posts':posts})
