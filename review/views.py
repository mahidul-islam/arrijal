from django.shortcuts import render
from .models import Review
from .forms import ReviewForm
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.



def review(request):
    if request.user.is_authenticated:
        name= request.user.username
        u= User.objects.get(username=name)
    template = loader.get_template('review/review.html')
    review = Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
        last=str(Review.objects.latest('id'))
        Review.objects.filter(id=last).update(user=u)
        return redirect('review:review')
    else:
        form = ReviewForm

    if request.user.is_authenticated:
        context = {'form':form , 'review':review, 'u':u }
    else:
        context = {'form':form , 'review':review }
    return HttpResponse(template.render(context,request))


def edit(request,id):
    template = loader.get_template('review/edit.html')
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review:review')
    else:
        form = ReviewForm(instance=review)
    context = {'form':form }
    return HttpResponse(template.render(context,request))



def delete(request,id):
    review = Review.objects.get(id=id)
    review.delete()
    return redirect('review:review')
