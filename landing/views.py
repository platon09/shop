from django.shortcuts import render
from products.models import *

# Create your views here.
def landing(request):

	return render(request, 'landing/landing.html', locals())


def home(request):
	products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
	products_images_vegetables = products_images.filter(product__category__id=1)
	products_images_fruits = products_images.filter(product__category__id=2)
	products_images_meat = products_images.filter(product__category__id=3)
	return render(request,'landing/home.html', locals())	