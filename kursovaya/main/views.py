from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from languages.models import *
from django.views.generic import UpdateView


def mainpage(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    response = render(request, 'main/main.html')
    response.set_cookie('last_page', 'main')
    response.set_cookie('lastpage', 'main/main.html')
    return response


def register(request):
    mistakes = ''
    if request.method == 'POST':
        if 'register' in request.POST:
            if request.POST.get('password') == request.POST.get('password_check'):
                new_user = User()
                new_user.username = request.POST.get('username')
                new_user.set_password(request.POST.get('password'))
                new_user.email = request.POST.get('email')
                new_user.save()
                return redirect(request.COOKIES['last_page'])
            elif request.POST.get('password') != request.POST.get('password_check'):
                mistakes = 'Passwords aren\'t equal'
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    data = {'mistakes': mistakes}
    return render(request, 'main/register.html', data)


def login_user(request):
    mistakes = ''
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST.get('log_username')
            password = request.POST.get('log_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(request.COOKIES['last_page'])
                else:
                    mistakes = 'User isn\'t active'
            else:
                mistakes = 'No user found'
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    data = {'mistakes': mistakes}
    return render(request, 'main/login.html', data)


def search_template(request, word):
    data = {'word': word}
    return render(request, 'main/search.html', data)


def logout_user(request):
    logout(request)
    return redirect(request.COOKIES['last_page'])




