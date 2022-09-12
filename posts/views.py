from multiprocessing import context
from re import template
from django.shortcuts import render
from django.shortcuts import reverse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 
from main.models import User
from django.shortcuts import redirect
from .models import Post, Comment
from .forms import (
    PostModelForm,
    CommentForm
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
        post.is_tweet = True
        post.user = poster
        post.save()
        return super(CreatePostView, self).form_valid(form)

class PostListView(ListView):
    
    template_name = "posts/postlist.html"
    context_object_name = "posts"
    paginate_by = 1
    model = Post
    model = User
    def get(self, request):
        posts = Post.objects.all()
        form = PostModelForm()
        context={
            'posts':posts,
            'form':form
        }
        return render(request, 'posts/postlist.html',context)


class AddLike(TemplateView):
     def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        is_like = False
        likes = post.likes.all()
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        if not is_like:
                post.likes.add(request.user)
        if is_like:
                post.likes.remove(request.user)
        like_count = len(likes)
    
    
class RemoveLike(TemplateView):
     def post(self, request, pk, *args, **kwargs):
        profile = Post.objects.get(pk=pk)
        profile.likes.add(request.user)
        return redirect('posts:postlist')
    
class Comments(ListView):
    template_name = "posts/comments.html"
    context_object_name = "comments"
    model = Comment
    paginate_by = 1
    model = Post
    def get(self, request, pk):
        comments = Comment.objects.filter(post_id = pk)
        posts = Post.objects.filter(pk = pk)
        form = CommentForm()

        context = {
            'comments':comments,
            'posts':posts,
            'form':form,
        }
        return render(request, 'posts/comments.html',context)


class CreateComment(CreateView):
    template_name = "posts/comments.html"
    form_class = CommentForm
    def get_success_url(self):
        
        return reverse("posts:comments", args=[self.kwargs['pk']])

    def form_valid(self, form):
        pk= self.kwargs['pk']
        author = self.request.user
        postid = pk
        comment = form.save(commit=False)
        comment.post_id = postid
        comment.author = author
        comment.save()
        return super(CreateComment, self).form_valid(form)
