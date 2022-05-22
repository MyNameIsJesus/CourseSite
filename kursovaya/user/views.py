from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateUserProfileForm
from django.core.files.base import ContentFile
from languages.models import *
from PIL import Image
import io


def userpage(request, pk):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    user = User.objects.filter(id=pk)
    data = {'User':user}
    response = render(request, 'user/userpage.html', data)
    response.set_cookie('last_page', 'userpage')
    response.set_cookie('lastpage', 'user/userpage.html')
    return response


# class UserUpdateView(UpdateView):
#     template_name = 'main/register.html'
#     model = User
#     context_object_name = 'user'
#     fields = ['username', 'password', 'email',]

@login_required
def UserUpdate(request, pk):
    mistakes = ''
    if request.method == 'POST':
        user = User.objects.filter(username= request.user.username)[0]
        if request.POST.get('username'):
            user.username = request.POST.get('username')
        if request.user.password != request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        if request.POST.get('email'):
            user.email = request.POST.get('email')
        if request.FILES.get('avatar'):
            ava = request.FILES.get('avatar')
            # im = Image.open(ava)
            # namefile = im.filename
            # im = im.convert('RGB')
            # im.thumbnail((300,300), Image.ANTIALIAS)
            # img_io = io.BytesIO()
            # im.save(img_io, format='JPEG', quality=60)
            # user.userprofile.avatar.save(namefile.split(r'/')[-1], ContentFile(img_io.getvalue()), save=False)
            # new_file = ContentFile(ava)
            # new_file.name = user.username
            user.userprofile.avatar = ava

        user.save()
        return redirect('main')
    userform = UpdateUserForm(instance=request.user)
    userprofileform = UpdateUserProfileForm(instance=request.user.userprofile)
    data ={'userform': userform, 'userprofileform': userprofileform, 'mistakes': mistakes, 'pass':request.user.password}
    return render(request, 'user/userupdate.html', data)
# Create your views here.
