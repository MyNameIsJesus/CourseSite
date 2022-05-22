from django.urls import path
from . import views

urlpatterns = [
    path('CSharp', views.CSharp, name='C#'),
    path('Python', views.Python, name='Python'),
    path('C++', views.CPlus, name='C++'),
    path('PHP', views.Php, name='PHP'),
    path('Kotlin', views.Kotlin, name='Kotlin'),
    path('Java', views.Java, name='Java'),
    path('create', views.create, name='create'),
    path('articles/<int:pk>', views.PostDetailView.as_view(), name='Article'),
    path('articles/<int:pk>/update', views.PostUpdateView, name='update_article'),
    path('articles/create', views.createarticle, name='create_article'),
    path('articles/<int:pk>/delete', views.PostDeleteView.as_view(), name='delete_article'),
    path('discussion/create', views.creatediscuss, name='create_discuss'),
    path('discussion/<int:pk>', views.DiscussDetailView.as_view(), name='discuss'),
    path('discussion/<int:pk>/update', views.DiscussUpdateView, name='update_discuss'),
    path('discussion/<int:pk>.delete', views.DiscussDeleteView.as_view(), name='delete_discuss'),
]