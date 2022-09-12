
from ast import ListComp
from typing import List
from urllib import request
from django.shortcuts import render, redirect
from main.models import User, UserProfile
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.generic import (
    TemplateView, 
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView,
    FormView,
    
)  
from posts.models import Post
from .forms import CustomUserChangeForm

class UserView(ListView):
    
    template_name = "user/user.html"
    context_object_name = "posts"
    model = User
    model = Post
    def get(self, request, *args, **kwargs):
        pk=self.request.user.pk
        profile = User.objects.get(pk=pk)
        posts = Post.objects.filter(user=self.request.user)
        users = User.objects.filter(pk=pk)
        followers = profile.followers.all()
        following = profile.following.all()

        number_of_followers = len(followers)
        number_of_following = len(following)

        context={
            'users':users,
            'posts':posts,
            'number_of_followers':number_of_followers,
            'number_of_following':number_of_following,
        }
        return render(request,'user/user.html', context)
    

class PublicProfileView(ListView):
    template_name = "user/public_profile.html"
    context_object_name = "posts"
    model = User
    model = Post
    def get(self, request, pk, *args, **kwargs):
        profile = User.objects.get(pk=pk)
        posts = Post.objects.filter(user=pk)
        users = User.objects.filter(pk=pk)
        followers = profile.followers.all()
        following = profile.following.all()

        number_of_followers = len(followers)
        number_of_following = len(following)
        if len(followers) == 0:
            is_following = False
            
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                 is_follower = False
                 break

        context={
            'users':users,
            'posts':posts,
            'number_of_followers':number_of_followers,
            'is_following':is_following,
            'number_of_following':number_of_following
        }
        return render(request,'user/public_profile.html', context)

class AddFollower(TemplateView):
    def post(self, request, pk, *args, **kwargs):
        profile = User.objects.get(pk=pk)
        self_profile = User.objects.get(pk=request.user.pk)
        self_profile.following.add(request.user)
        profile.followers.add(request.user)
        return redirect('user:public-profile', pk = profile.pk)

class RemoveFollower(TemplateView):
    def post(self, request, pk, *args, **kwargs):
        profile = User.objects.get(pk=pk)
        self_profile = User.objects.get(pk=request.user.pk)
        self_profile.following.remove(request.user)
        profile.followers.remove(request.user)
        return redirect('user:public-profile', pk = profile.pk)


class PostList(ListView):
    
    template_name = "user/postlist2.html"
    context_object_name = "posts"
    paginate_by = 1
    model = Post
    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)

class EditProfileView(UpdateView):

    form_class = CustomUserChangeForm
    template_name = "edit-profile.html"
            
    def get_queryset(self):
        pk = self.request.user.pk
        return User.objects.filter(pk=pk)
    
    def get_success_url(self):
        return reverse("user:profile")

    