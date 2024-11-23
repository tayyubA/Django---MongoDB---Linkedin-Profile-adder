from django.shortcuts import render
from .models import Profile


def create_profile(request):
    if request.method == 'POST':
        data = request.POST
        profile = Profile(
            name=data['name'],
            email=data['email'],
            headline=data['headline'],
            skills=data.getlist('skills'),
            
        )
        profile.save()
        
        
        return render(request, 'profiles/success.html', {'message': 'Profile created successfully!'})
    
    return render(request, 'profiles/create_profile.html')



def get_profiles(request):
    profiles = Profile.objects.all()
    #print(profiles)
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

def home(request):
    return render(request, 'profiles/home.html')