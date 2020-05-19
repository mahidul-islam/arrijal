from django.shortcuts import render

# Create your views here.
from .models import BlogPage
from .models import BlogCategory
from .models import BlogTagIndexPage
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render

from wagtail.core.models import Page
from wagtail.search.models import Query


def blogpage(request):
    tag1=' '
    li=[]
    posts=BlogPage.objects.all()
    posts2=BlogPage.objects.all()
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

    for page in posts2:
        for tag in page.tags.all():
            if tag1 != tag :
                tag1=tag
                li.append(tag1)


    res = []
    for i in li:
         if i not in res:
             res.append(i)


    return render(request,'blog/blog_index_page.html',{'posts':posts,'mylist':res,'categori':category})
def search(request):
    # Search
    search_query = request.GET.get('query', None)
    posts=BlogPage.objects.all()
    category=BlogCategory.objects.all()
    if search_query:
        search_results = BlogPage.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = BlogPage.objects.none()

    # Render template
    return render(request, 'blog/search_results.html', {
        'search_query': search_query,
        'search_results': search_results,
        'posts2':posts,'categori':category
    })

def category_dao(request,category_id):
    tag1=' '
    li=[]
    posts=[]
    single_category=BlogCategory.objects.get(pk=category_id)
    categories=BlogCategory.objects.all()
    l2=BlogPage.objects.all()
    print(type(l2))
    for page2 in l2:
        categor=page2.categories.all()
        for category in categor:
            if(single_category== category):
                 posts.append(page2)


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

    for page in l2:
        for tag in page.tags.all():
            if tag1 != tag :
                tag1=tag
                li.append(tag1)


    res = []
    for i in li:
         if i not in res:
             res.append(i)

    return render(request,'blog/category.html',{'categori':categories,'posts':posts,'mylist':res})
