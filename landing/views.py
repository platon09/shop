from django.shortcuts import render
from products.models import *

# Create your views here.
def landing(request):

	return render(request, 'landing/landing.html', locals())


def home(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True)
	return render(request,'landing/home.html', locals())