from django.shortcuts import render, get_object_or_404
from  .models import UserProfile
# Create your views here.

def home(request):
    return render(request, 'home.html')


def Profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})


def Pofile_detail(request, pk):
    profile = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'profile_detail.html', {'profile': profile})