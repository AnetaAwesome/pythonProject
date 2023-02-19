from django.urls import path, reverse_lazy
from django.views.generic import CreateView, DetailView
from . import views
from . import models

urlpatterns = [
    path('main_paige/', views.BlogPostView.as_view()),
    path('create/blog_post/', views.BlogPostCreate.as_view()),
    path('blog_post/<int:pk>/', DetailView.as_view(model=models.BlogPost, template_name='blog_app/post_detail.html'),
         name='blogpost_detail'),
]