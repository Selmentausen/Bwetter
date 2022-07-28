from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .forms import RegisterForm


# Create your views here.
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {'profiles': profiles})


def profile(request, pk):
    viewing_profile = Profile.objects.get(pk=pk)
    if request.method == 'POST':
        current_user_profile = request.user.profile
        action = request.POST.get('follow')
        if action == 'follow':
            current_user_profile.follows.add(viewing_profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(viewing_profile)
        current_user_profile.save()
    return render(request, 'profile.html', {'profile': viewing_profile})


def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        return redirect('login')
    return render(request, 'register.html', {'form': form})
