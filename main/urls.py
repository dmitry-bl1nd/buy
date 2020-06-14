from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import static
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	# path('test', views.test, name = 'test'),
	path('sell', views.sell, name= 'sell')
]

if settings.DEBUG:
	urlpatterns += static (settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)