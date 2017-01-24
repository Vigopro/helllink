from .models import ShortURL
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})


class ShortCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

