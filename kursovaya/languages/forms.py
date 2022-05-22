from .models import Article, Discuss, Comments
from django.forms import TextInput, Textarea, ModelForm, DateInput, IntegerField, CharField, Select, MultipleHiddenInput
from datetime import datetime

languages_list = (("Python","Python"),
                  ("C#", "C#"),
                  ("C++", "C++"),
                  ("Kotlin", "Kotlin"),
                  ("Java", "Java"),
                  ("PHP", "PHP"))


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'announce', 'full_text', 'language', 'date', 'author']
        widgets = {'title': TextInput(attrs ={'class':'form-control', 'placeholder':'title'}),
                   'announce': TextInput(attrs={'class':'form-control', 'placeholder':'your announce'}),
                   'full_text': Textarea(attrs={'class':'form-control', 'placeholder':'text'}),
                   'author': TextInput(attrs={'class':'form-control', 'id': 'author', 'value':'1', 'type':'hidden'}),
                   'date': DateInput(attrs={'class':'form-control', 'value':datetime.now(), 'type':'hidden'}),
                   'language': Select(choices=languages_list),

                   }


class DiscussForm(ModelForm):
    class Meta:
        model = Discuss
        fields = ['title', 'question', 'language', 'date', 'author']
        widgets = {'title': TextInput(attrs={'class':'form-control', 'placeholder':'Your question'}),
                   'question': Textarea(attrs={'class': 'form-control', 'placeholder':'Details'}),
                   'date': DateInput(attrs={'class':'form-control', 'type':'hidden', 'value':datetime.now()}),
                   'author': TextInput(attrs={'class':'form-control', 'type':'hidden', 'id':'author1', 'value':'1'}),
                   'language': Select(choices=languages_list)
                  }


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['post', 'user', 'language', 'text', 'date', 'rating']
        widgets = {'post':TextInput(attrs={'class':'form-control'}),
                   'user':TextInput(attrs={'class':'form-control', 'placeholder':'User'}),
                   'language':TextInput(attrs={'class':'form-control','placeholder':'Language'}),
                   'text':TextInput(attrs={'class': 'form-control', 'placeholder':'Text'}),
                   'rating':IntegerField()
                   }
