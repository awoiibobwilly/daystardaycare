from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def secondlanding(request):
    template = loader.get_template ('secondlanding.html')
    return HttpResponse(template.render())
