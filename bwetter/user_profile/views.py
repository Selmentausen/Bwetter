from django.shortcuts import render
from .models import Profile


# Create your views here.
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, 'profile_list.html', {'profiles': profiles})
