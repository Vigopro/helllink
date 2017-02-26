from .forms import SubmitUrlForm
from .models import ShortURL
from analytics.models import ClickCounter
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortener/home.html", {})

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()

        context = {
            "title": "Submit URL",
            "form": form,
        }

        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Submit URL",
            "form": form,
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ShortURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = ShortURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exist():
            raise Http404
        obj = qs.first()
        print(ClickCounter.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


