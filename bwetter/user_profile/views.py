from django.shortcuts import render
from .models import Profile


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
