from .models import Subs
from django.forms import ModelForm, TextInput, DateInput


class SubsForm(ModelForm):
    class Meta:
        fields = '__all__'
        model = Subs
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subscription name'
            }),
            "cost": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subscription cost'
            }),
            "distributor": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subscription distributor'
            }),
            "start_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subscription date'
            }),
        }
