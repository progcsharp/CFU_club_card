# places/views.py

from django.shortcuts import render, get_object_or_404

from .forms import PlaceFilterForm
from .models import Place


def place_list(request):
    form = PlaceFilterForm(request.GET or None)
    places = Place.objects.all()

    if form.is_valid():
        if form.cleaned_data['name']:
            places = places.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['category']:
            places = places.filter(category=form.cleaned_data['category'])

    return render(request, 'places/place_list.html', {'form': form, 'places': places})


def place_detail(request, place_id):
    place = Place.objects.get(pk=place_id)  # Предзагрузка изображений и адресов
    return render(request, 'places/place_detail.html', {'place': place})

