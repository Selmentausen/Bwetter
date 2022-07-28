from django.shortcuts import render, redirect
from .forms import PostForm, CommentForm
from .models import Post, Comment


# Create your views here.
def dashboard(request):
    posts = []
    if request.user.is_authenticated:
        print('hello')
        posts = Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})


def post_index(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST or None)
    return render(request, 'post_index.html', {'post': post, 'form': form})


def new_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:dashboard')
    return render(request, 'new_post.html', {'form': form})


def comment_add(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid() and post:
            comment = Comment(post=post, user=request.user, text=form.cleaned_data['text'])
            comment.save()
    return redirect("posts:post_index", post_pk)


def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect("posts:post_index", post_pk)
