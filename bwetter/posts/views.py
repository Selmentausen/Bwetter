from django.shortcuts import render, redirect
from .forms import PostForm


# Create your views here.
def dashboard(request):
    posts = []
    for profile in request.user.profile.follows.all():
        for post in profile.user.posts.all():
            posts.append(post)
    posts = sorted(posts, key=lambda s: s.created_date, reverse=True)
    return render(request, 'post_list.html', {'posts': posts})


def new_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:dashboard')
    return render(request, 'new_post.html', {'form': form})

