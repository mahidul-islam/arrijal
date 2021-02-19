from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import NewsletterUser
from django.contrib import messages

# from .forms import NewsletterUserForm

def subscribe(request):
    if request.method == 'POST':
        data = request.POST.get('email')
        if NewsletterUser.objects.filter(email=data).exists():
            messages.add_message(request, messages.INFO, 'Mail Already in the List.')
        else:
            new_user = NewsletterUser(email=data, user=request.user)
            new_user.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added mail to subscribed list')

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
