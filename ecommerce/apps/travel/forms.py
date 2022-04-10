from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm
)

from .models import (
    Company,
    Place,
    Service,
    Travel
)


class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre de la empresa',
        min_length=4,
        max_length=255,
        help_text='Required',
    )

    razon_social = forms.CharField(
        label='Razon Social',
        min_length=1,
        max_length=255,
        help_text='Required')

    nit = forms.CharField(
        label='NIT',
        min_length=1,
        max_length=50,
        help_text='Required')

    class Meta:
        model = Company
        fields = ('name','razon_social','nit')

    #
    # def clean_nit(self):
    #     nit = self.cleaned_data['nit'].upper().strip()
    #     r = Company.objects.filter(nit=nit)
    #     if r.count():
    #         raise forms.ValidationError("El NIT ya existe.")
    #     return nit

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nombre de la empresa'})
        self.fields['razon_social'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Razon Social'})
        self.fields['nit'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'NIT'})


class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ('name','address','img_l','latitude','longitude',)
        widgets={
            'img_l': forms.FileInput(attrs={'style': 'display: block;', 'class': 'form-control', 'required': False, })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Nombre del lugar'})
        self.fields['address'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Direccion'})
        self.fields['latitude'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'GPS' ,'readonly':'true'})
        self.fields['longitude'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'GPS','readonly':'true'})


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = (
            'name',
            'origin',
            'destination',
            'price',
            'description',
            'img_l',
        )
        widgets={
            'name' : forms.TextInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
            'origin': forms.Select(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
            'destination': forms.Select(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
            'price': forms.NumberInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
            'description': forms.Textarea(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
            'img_l': forms.FileInput(attrs={'style': 'display: block;', 'class': 'form-control', })
        }
import datetime

class TravelForm(forms.ModelForm):
    # time_departure = forms.DateTimeField(initial=datetime.date.today)
    class Meta:
        model = Travel
        fields = (
            'service',
            'time_departure',
            'time_arrival_destination',
            'time_departure_return',
            'time_arrival_return',
            'travel_type',
            'passengers_limit',
        )
        widgets={
        'service' : forms.HiddenInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'time_departure' : forms.DateTimeInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'time_arrival_destination' : forms.DateTimeInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'time_departure_return' : forms.DateTimeInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'time_arrival_return' : forms.DateTimeInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'travel_type' : forms.Select(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        'passengers_limit' : forms.NumberInput(attrs={'style': 'display: block;', 'class': 'form-control mb-3' }),
        }