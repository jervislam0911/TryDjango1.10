from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import KirrURL



# Create your views here.
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
	obj = KirrURL.objects.get(shortcode=shortcode)
	return HttpResponse('hello {sc}'.format(sc=obj.url))


class KirrCBView(View):
	def get(self,request, shortcode=None, *args, **kwargs):
		return HttpResponse('hello again {sc}'.format(sc=shortcode))
		