from .models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

def redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ShortURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)

class ShortCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return HttpResponse()


'''
    # obj = ShortURL.objects.get(shortcode=shortcode)
    obj_url = obj.url
    try:
        obj = ShortURL.objects.get(shortvode=shortcode)
    except:
        obj = ShortURL.objects.all().first()

    obj_url = None
    qs = ShortURL.objects.filter(shortcode__iexact=shortcode.upper())
    if qs.exists() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url

'''




