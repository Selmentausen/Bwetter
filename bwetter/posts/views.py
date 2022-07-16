from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


# Create your views here.
def dashboard(request):
    posts = []
    if request.user.is_authenticated:
        print('hello')
        posts = Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by('created_date')
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

