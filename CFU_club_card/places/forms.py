from django import forms
from .models import Place, Category

class PlaceFilterForm(forms.Form):
    name = forms.CharField(
        required=False,
        label='Название',
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full p-2 border border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-gray-700 text-white',
        }))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),

        required=False,
        label='Категория',
        widget=forms.Select(attrs={
            'class': 'mt-1 block w-full p-2 border border-gray-600 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 sm:text-sm bg-gray-700 text-white',
        })
    )
