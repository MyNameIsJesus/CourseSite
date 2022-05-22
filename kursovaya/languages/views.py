from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView, UpdateView
from .forms import ArticleForm, DiscussForm, CommentsForm
from datetime import date


def CSharp(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles = Article.objects.filter(language='C#')
    discuss = Discuss.objects.filter(language='C#')
    response = render(request, 'languages/C#.html', {'articles': articles, 'discuss': discuss})
    response.set_cookie('last_page', 'C#')
    response.set_cookie('lastpage', 'languages/C#.html')
    return response


def Kotlin(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles =Article.objects.filter(language='Kotlin')
    discuss = Discuss.objects.filter(language='Kotlin')
    response = render(request, 'languages/Kotlin.html', {'articles':articles, 'discuss': discuss})
    response.set_cookie('last_page', 'Kotlin')
    response.set_cookie('lastpage', 'languages/Kotlin.html')
    return response


def Java(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles =Article.objects.filter(language='Java')
    discuss = Discuss.objects.filter(language='Java')
    response = render(request, 'languages/Java.html', {'articles':articles, 'discuss':discuss})
    response.set_cookie('last_page', 'Java')
    response.set_cookie('lastpage', 'languages/Java.html')
    return response


def Php(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles =Article.objects.filter(language='PHP')
    discuss = Discuss.objects.filter(language='PHP')
    response = render(request, 'languages/PHP.html', {'articles':articles, 'discuss': discuss})
    response.set_cookie('last_page', 'PHP')
    response.set_cookie('lastpage', 'languages/PHP.html')
    return response


def Python(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles =Article.objects.filter(language='Python')
    discuss = Discuss.objects.filter(language='Python')
    response = render(request, 'languages/Python.html', {'articles':articles, 'discuss': discuss})
    response.set_cookie('last_page', 'Python')
    response.set_cookie('lastpage', 'languages/Python.html')
    return response


def CPlus(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    articles =Article.objects.filter(language='C++')
    discuss = Discuss.objects.filter(language='C++')
    response = render(request, 'languages/C++.html', {'articles':articles, 'discuss': discuss})
    response.set_cookie('last_page', 'C++')
    response.set_cookie('lastpage', 'languages/C++.html')
    return response


class PostDetailView(DetailView):
    template_name = 'languages/detail_view.html'
    model = Article
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        pk = request.POST.get('id1')
        if 'comment-post' in request.POST:
            comment = Comments()
            if request.user.is_authenticated:
                comment.user = request.user.username
                comment.text = request.POST.get('text')
                comment.language=request.POST.get('language1')
                comment.date = date.today()
                comment.post = request.POST.get('title1')
                comment.save()
                return redirect('Article', pk=pk)
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
        elif 'like' in request.POST:
            pk = request.POST.get('id1')
            article = Article.objects.get(id=pk)
            author1 = User.objects.get(username=article.author)
            if article.dislikes.filter(username=request.user).exists():
                author1.userprofile.rating += 2
                article.dislikes.remove(request.user)
            else:
                author1.userprofile.rating += 1
            author1.save()
            article.likes.add(request.user)
            return redirect('Article', pk=int(pk))
        elif 'dislike' in request.POST:
            pk = request.POST.get('id1')
            article = get_object_or_404(Article, id=pk)
            author = User.objects.get(username=article.author)
            if article.likes.filter(username=request.user).exists():
                author.userprofile.rating -= 2
                article.likes.remove(request.user)
            else:
                author.userprofile.rating -= 1
            article.dislikes.add(request.user)
            author.save()
            return redirect('Article', pk=int(pk))

    def get_context_data(self, **kwargs):
        article = Article.objects.get(pk=self.kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        if self.request.user in article.likes.all():
            context['user_liked'] = True
        if self.request.user in article.dislikes.all():
            context['user_disliked'] = True
        return context


class PostDeleteView(DeleteView):
    template_name = 'languages/delete.html'
    model = Article
    context_object_name = 'article'
    success_url = '/'


def PostUpdateView(request, pk):
    article = Article.objects.get(pk=pk)
    data = {'obj': article}
    if request.method == 'POST':
        if 'update-article' in request.POST:
            article.title = request.POST.get("new_title")
            article.announce = request.POST.get("new_announce")
            article.full_text = request.POST.get("new_text")
            article.full_text = request.POST.get("new_text")
            article.save()
            return redirect('Article', pk=pk)
    return render(request, 'languages/update.html', data)
# class PostUpdateView(UpdateView):
#     template_name = 'languages/update.html'
#     model = Article
#     form_class = ArticleForm
#     context_object_name = 'article'
#
#     def post(self, request, *args, **kwargs):
#
#
#     def form_invalid(self, form):
#         print("form is invalid")
#         return HttpResponse(form.errors)


def createarticle(request):
    error = ''
    if request.method == 'POST':
        if 'article-post' in request.POST:
            form = ArticleForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user.username
                instance.save()
                return redirect(request.COOKIES['last_page'])
            else:
                error = form.errors
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    form = ArticleForm()
    data = {'form': form, 'error': error}
    return render(request, 'languages/create.html', data)


class DiscussDetailView(DetailView):
    template_name = 'languages/detail_view_discuss.html'
    model = Discuss
    context_object_name = 'discuss'

    def render_to_response(self, context, **response_kwargs):
        response = super(DetailView, self).render_to_response(context, **response_kwargs)
        response.set_cookie('last_page', 'Article')
        response.set_cookie('lastpage', 'languages/detail_view.html')
        return response

    def post(self, request, *args, **kwargs):
        if 'comment-post' in request.POST:
            pk=request.POST.get('id1')
            comment = Comments()
            if request.user.is_authenticated:
                comment.user = request.user.username
            comment.text = request.POST.get('text')
            comment.language=request.POST.get('language1')
            comment.date = date.today()
            comment.post = request.POST.get('id1')
            comment.save()
            return redirect('discuss', pk=pk)
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
        elif 'choose_correct' in request.POST:
            pk = request.POST.get('id1')
            post_id = request.POST.get('comment-id')
            comments = Comments.objects.get(id=post_id)
            user_correct = User.objects.get(username=comments.user)
            if comments.is_correct == True:
                comments.is_correct = False
                user_correct.userprofile.rating -=1
                user_correct.save()
                comments.save()
                return redirect('discuss', pk=pk)
            for i in Comments.objects.filter(post=pk):
                i.is_correct = False
                i.save()
            comments.is_correct = True
            user_correct.userprofile.rating += 1
            user_correct.save()
            comments.save()
            return redirect('discuss', pk=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.all()
        return context

# def post_detail_view(request, pk):
#     if request.method == 'POST':
#         form = CommentsForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#     form = CommentsForm()
#     data = {'discuss': Discuss, 'Comments':Comments, 'form':form}
#
#     return render(request, 'languages/detail_view_discuss.html', data)


def DiscussUpdateView(request, pk):
    discuss = Discuss.objects.get(pk=pk)
    data = {'obj': discuss}
    if request.method == 'POST':
        if 'update-article' in request.POST:
            discuss.title = request.POST.get("new_title")
            discuss.question = request.POST.get("new_announce")
            discuss.save()
            return redirect('Discuss', pk=pk)
    return render(request, 'languages/update1.html', data)


def creatediscuss(request):
    if request.method == 'POST':
        form = DiscussForm(request.POST)
        if 'create-discuss' in request.POST:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user.username
                instance.save()
                return redirect(request.COOKIES['last_page'])
        elif 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles':articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    form = DiscussForm
    data = {'form':form}
    return render(request, 'languages/create_disc.html', data)


class DiscussDeleteView(DeleteView):
    template_name = 'languages/delete.html'
    model = Discuss
    context_object_name = 'article'
    success_url = "/"


def create(request):
    if request.method == 'POST':
        if 'search-post' in request.POST:
            search = request.POST.get('search')
            articles = Article.objects.all()
            discuss = Discuss.objects.all()
            dat = {'search': search, 'articles': articles, 'discuss': discuss}
            response = render(request, 'main/search.html', dat)
            return response
    return render(request, 'languages/choose_create.html')

