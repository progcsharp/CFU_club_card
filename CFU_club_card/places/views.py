# places/views.py

from django.shortcuts import render, get_object_or_404
from .models import Place

def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})


def place_detail(request, place_id):
    place = Place.objects.get(pk=place_id)  # Предзагрузка изображений и адресов
    print(place.addresses)
    return render(request, 'places/place_detail.html', {'place': place})

