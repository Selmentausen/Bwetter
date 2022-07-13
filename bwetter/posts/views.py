from django.shortcuts import render


# Create your views here.
def dashboard(request):
    posts = []
    for profile in request.user.profile.follows.all():
        for post in profile.user.posts.all():
            posts.append(post)
    posts = sorted(posts, key=lambda s: s.created_date, reverse=True)
    return render(request, 'post_list.html', {'posts': posts})
