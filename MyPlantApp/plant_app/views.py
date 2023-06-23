from django.shortcuts import render, redirect

from MyPlantApp.account.models import Profile
from MyPlantApp.plant_app.forms import PlantAppForm, DeletePlant
from MyPlantApp.plant_app.models import PlantApp


# Create your views here.

def home(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, template_name='templates/plant_app/home-page.html', context=context)


def catalogue(request):
    plants = PlantApp.objects.all()
    context = {'plants': plants}
    return render(request, template_name='templates/plant_app/catalogue.html', context=context)


def create_plant(request):
    form = PlantAppForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {'form': form}
    return render(request, template_name='templates/plant_app/create-plant.html', context=context)


def plant_details(request, plant_id):
    plant = PlantApp.objects.get(id=plant_id)
    context = {'plant': plant}
    return render(request, template_name='templates/plant_app/plant-details.html', context=context)


def edit_plant(request, plant_id):
    plant = PlantApp.objects.get(id=plant_id)

    if request.method == 'GET':
        context = {'form': PlantAppForm(initial=plant.__dict__)}
        return render(request, template_name='templates/plant_app/edit-plant.html', context=context)

    else:
        form = PlantAppForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
        else:
            context = {'form': form}
            return render(request, template_name='templates/plant_app/edit-plant.html', context=context)


def delete_plant(request, plant_id):
    plant = PlantApp.objects.get(id=plant_id)
    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')
    form = DeletePlant(instance=plant)
    context = {'form': form}
    return render(request, template_name='templates/plant_app/delete-plant.html', context=context)
