from django.urls import path, reverse_lazy
from django.views.generic import CreateView
from . import views
from . import models

urlpatterns = [
    path('create/post/', views.BlogPostCreate.as_view()),
]