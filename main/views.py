from django.shortcuts import render
from .models import Building
from .forms import AddBuilding

def index(request):
	buildings = Building.objects.all()
	return render(request, 'home.html', {'buildings' : buildings})

def test(request):
	buildings = Building.objects.all()
	return render(request, 'test.html', {'buildings': buildings})

def sell(request):
	if request.method == 'POST':
		form = AddBuilding(request.POST)
		if form.is_valid():
			type = form.cleaned_data['type']
			price = form.cleaned_data['price']
			img = form.cleaned_data['img']
			area = form.cleaned_data['area']
			location = form.cleaned_data['location']
			date = form.cleaned_data['date']
	else:
		form = AddBuilding()

	form = AddBuilding()
	return render(request, 'sell.html', {'form' : form})