from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def adminsecsignin(request):
    template = loader.get_template ('adminsecsignin.html')
    return HttpResponse(template.render())
