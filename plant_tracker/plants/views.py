from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant
from .forms import PlantForm

# Create + View All
def plant_list(request):
    plants = Plant.objects.all()
    return render(request, 'plants/list.html', {'plants': plants})


# Create
def add_plant(request):
    if request.method == "POST":
        form = PlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm()
    return render(request, 'plants/add.html', {'form': form})


# Update
def edit_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    if request.method == "POST":
        form = PlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('plant_list')
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plants/edit.html', {'form': form})


# Delete
def delete_plant(request, pk):
    plant = get_object_or_404(Plant, pk=pk)
    plant.delete()
    return redirect('plant_list')
