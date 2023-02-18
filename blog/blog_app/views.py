
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView
from blog_app.models import BlogPost
from blog_app import forms


class BlogPostCreate(CreateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'blog_app/create_post_view.html'

    # def get_success_url(self):
    #     return reverse('', kwargs={'pk': self.object.pk})

