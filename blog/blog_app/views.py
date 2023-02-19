
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import BlogPost

class BlogPostView(TemplateView):
    template_name = 'blog_app/main_paige.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class BlogPostCreate(CreateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'blog_app/create_post_view.html'

    def get_success_url(self):
        return reverse('blogpost_detail', kwargs={'pk': self.object.pk})

