# Ваш_проект/forms.py
from django import forms
from .models import Location

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Location  # Замените на вашу модель, в которой вы хотите хранить данные
        fields = ['name', 'lastname', 'mobile_number', 'region1', 'services']

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write your name:', 'class': 'input'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write your lastname', 'class': 'input'}))
    mobile_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Write your mobile number', 'class': 'input'}))
    region1 = forms.ChoiceField(choices=[('Argentina', 'Argentina'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'),
                                        ('Chile', 'Chile'), ('Colombia', 'Colombia'), ('Ecuador', 'Ecuador'),
                                        ('Guyana', 'Guyana'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'),
                                        ('Suriname', 'Suriname'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela')],
                               widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Select region'}))
    services = forms.ChoiceField(choices=[('Cargo', 'Cargo'), ('Plane', 'Plane'), ('Truck', 'Truck')],
                               widget=forms.Select(attrs={'class': 'select', 'placeholder': 'Select region'}))
