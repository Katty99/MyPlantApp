from django.shortcuts import render, redirect

from MyPlantApp.account.forms import ProfileForm, EditProfile
from MyPlantApp.account.models import Profile
from MyPlantApp.plant_app.models import PlantApp


# Create your views here.

def create_profile(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {'form': form}
    return render(request, template_name='templates/account/create-profile.html', context=context)


def profile_details(request):
    profile = Profile.objects.first()
    plants = len(PlantApp.objects.all())
    context = {
        'profile': profile,
        'plants': plants,
    }
    return render(request, template_name='templates/account/profile-details.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        context = {'form': EditProfile(initial=profile.__dict__)}
        return render(request, 'templates/account/edit-profile.html', context=context)
    else:
        form = EditProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
        else:
            context = {'form': form}
            return render(request, template_name='templates/account/edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.first()
    plants = PlantApp.objects.all()
    if request.method == 'POST':
        profile.delete()
        plants.delete()
        return redirect('home')
    return render(request, template_name='templates/account/delete-profile.html')
