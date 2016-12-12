from django.shortcuts import render, redirect
from . import models

def index(request):
    return render(request, 'mtm/index.html')

def users(request):
    users = models.User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'mtm/users.html', context)

def show(request, id):
    user_list = models.User.objects.filter(id=id)
    context = {
        'user': user_list[0]
    }
    return render(request, 'mtm/show.html', context)

def process(request):
    name = request.POST['name'].lower()
    user_list = models.User.objects.filter(name = name)
    if user_list:
        user = user_list[0]
    else:
        user = models.User.objects.create(name=name)

    interest = request.POST['interest'].lower()
    interest_list = models.Interest.objects.filter(name=interest)
    if interest_list:
        interest = interest_list[0]
    else:
        interest = models.Interest.objects.create(name=interest)

    user.interests.add(interest)
    return redirect('/users')






    return redirect('/')
# Create your views here.
