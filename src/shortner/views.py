from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm
        context = {
            "title":"Pagina Inicial",
            "form":form
        }
        return render(request, "shortner/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print (form.cleaned_data)
        context = {
            "title": "Nova Url",
            "form": form
        }
        return render(request, "shortner/home.html", context)


class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
