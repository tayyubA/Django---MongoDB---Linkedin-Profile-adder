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
        
        # After saving the profile, redirect to a new page that shows the success message
        return render(request, 'profiles/success.html', {'message': 'Profile created successfully!'})
    
    return render(request, 'profiles/create_profile.html')



# Retrieve profiles
def get_profiles(request):
    profiles = Profile.objects.all()
    #print(profiles)
    return render(request, 'profiles/profile_list.html', {'profiles': profiles})

