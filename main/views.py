from django.shortcuts import render
from .models import Building
def index(request):
	buildings = Building.objects.all()
	return render(request, 'main.html', {'buildings' : buildings})

def test(request):
	buildings = Building.objects.all()
	return render(request, 'test.html', {'buildings': buildings})
