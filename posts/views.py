from re import template
from django.shortcuts import render
from django.shortcuts import reverse

from django.http import HttpResponse 
from django.shortcuts import redirect
from .models import Post
from .forms import (
    PostModelForm
)
from django.views.generic import (
    TemplateView, 
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
    FormView
)

class CreatePostView(CreateView):
    template_name = "posts/createpost.html"
    form_class = PostModelForm
    def get_success_url(self):
        return reverse("postlist")

    def form_valid(self, form):
        poster = self.request.user
        post = form.save(commit=False)
        post.user = poster
        post.save()
        return super(CreatePostView, self).form_valid(form)

class PostListView(CreateView):
    
    template_name = "posts/postlist.html"
    context_object_name = "posts"
    form_class = PostModelForm

    model = Post
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

    def get_success_url(self):
        return reverse("postlist")

    def form_valid(self, form):
        poster = self.request.user
        post = form.save(commit=False)
        post.user = poster
        post.save()
        return super(PostListView, self).form_valid(form)