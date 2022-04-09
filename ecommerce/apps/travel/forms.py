from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm
)

from .models import Company


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

    # def clean_name(self):
    #     import pdb;pdb.set_trace()
    #     name = self.cleaned_data['name'].upper().strip()
    #
    #     field_name = 'name'
    #
    #     if self.instance:
    #         r = Company.objects.filter({'name':name}).exclude(id=self.instance.id)
    #     else:
    #         r = Company.objects.filter(name=name)
    #
    #     if r.count() :
    #         raise forms.ValidationError("El nombre de la empresa ya existe")
    #     return name
    #
    # def clean_razon_social(self):
    #     razon_social = self.cleaned_data['razon_social'].upper().strip()
    #     return razon_social
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
