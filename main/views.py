from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Building
from .forms import AddBuilding

def index(request):
	buildings = Building.objects.all()
	return render(request, 'home.html', {'buildings' : buildings})

def sell(request):
	if request.method == 'POST':
		form = AddBuilding(request.POST, request.FILES)
		if form.is_valid():
			print('Valid')
			obj = Building()
			obj.type = form.cleaned_data['type']
			obj.price = form.cleaned_data['price']
			obj.img = form.cleaned_data['img']
			obj.area = form.cleaned_data['area']
			obj.location = form.cleaned_data['location']
			obj.date = form.cleaned_data['date']
			obj.save()
			print('Saved')
			return HttpResponseRedirect('/')
	else:
		print('Else')
		form = AddBuilding()
	return render(request, 'sell.html', {'form' : form})