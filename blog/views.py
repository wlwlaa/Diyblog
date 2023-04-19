from django.shortcuts import render
from .models import Author, Post, User, Comment
from datetime import date
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms import forms


def index(request):
    num_of_authors = User.objects.all().count()
    num_of_posts = Post.objects.all().count()

    num_today_posts = Post.objects.filter(date_of_post=date.today()).count()
    num_today_comms = Comment.objects.filter(time_of_comment__date=date.today()).count()

    return render(
        request, 'index.html',
        context={
            'num_of_authors': num_of_authors,
            'num_of_posts': num_of_posts,
            'num_today_posts': num_today_posts,
            'num_today_comms': num_today_comms,
            }
        )


class PostListView(generic.ListView):
    model = Post
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.order_by('-date_of_post').all()

class PostDetailView(generic.DetailView):
    model = Post

class PostCreate(LoginRequiredMixin, generic.edit.CreateView):
    model = Post
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author


class CommentCreate(LoginRequiredMixin ,generic.edit.CreateView):
    model = Comment
    fields = ['comment_text']

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super(CommentCreate, self).form_valid(form)
    