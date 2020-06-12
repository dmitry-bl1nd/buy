from django import forms
from .models import Building
from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django import forms

class AddBuilding(forms.Form):
        type = forms.CharField(max_length=100)
        price = forms.IntegerField()
        img = forms.ImageField()
        area = forms.IntegerField()
        location = forms.CharField(max_length=25)
        date = forms.DateTimeField()