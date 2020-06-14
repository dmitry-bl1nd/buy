from django import forms
from django.contrib.admin import widgets
from timezone import timezone
import datetime

class AddBuilding(forms.Form):
        type = forms.CharField(initial='Квартира',max_length=100)
        price = forms.IntegerField(initial=20000000)
        img = forms.ImageField(allow_empty_file=True)
        area = forms.IntegerField(initial=200)
        location = forms.CharField(initial='Москва',max_length=25)
        date = forms.DateField(initial=timezone.now(),widget=forms.SelectDateWidget)