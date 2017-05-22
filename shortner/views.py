from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm
        context = {
            "title": "Encurte sua URL",
            "form": form
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Nova Url",
            "form": form
        }
        template = "shortner/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            if not (new_url.startswith('http://') or new_url.startswith('https://')):
                new_url = 'http://' + new_url
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created
            }
            if created:
                template = 'shortner/sucess.html'
            else:
                template = 'shortner/exists.html'

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)
