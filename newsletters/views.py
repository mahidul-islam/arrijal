from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import NewsletterUser
# from .forms import NewsletterUserForm

def subscribe(request):
    if request.method == 'POST':
        data = request.POST.get('email')
        print(data)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
