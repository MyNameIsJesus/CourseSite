from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse


class Article(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    announce = models.CharField('Announce', max_length=200)
    full_text = models.TextField('Full_text')
    date = models.DateTimeField('Date')
    language = models.CharField('Language', max_length=30)
    likes = models.ManyToManyField(User, related_name='likes_articles')
    dislikes = models.ManyToManyField(User, related_name='dislikes_articles')
    author = models.CharField('User', max_length=125)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'


class Discuss(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    question = models.TextField('Question', unique=True)
    date = models.DateTimeField('Date')
    author = models.CharField('User', max_length=50)
    likes = models.ManyToManyField(User, related_name='likes_discuss')
    dislikes = models.ManyToManyField(User, related_name='dislikes_discuss')
    language = models.CharField('Language', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Discussion'
        verbose_name_plural = 'Discussion'


class Comments(models.Model):
    rating = models.IntegerField('Rating', default=0)
    post = models.IntegerField('Post')
    user = models.CharField('User', max_length=50)
    language = models.CharField('Language', max_length=30)
    text = models.TextField('Text', max_length=400)
    is_correct = models.BooleanField(name='is_correct', default=False)
    date = models.DateTimeField('Date')

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

