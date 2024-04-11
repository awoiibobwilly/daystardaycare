from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def firstlanding(request):
    template = loader.get_template ('firstlanding.html')
    return HttpResponse(template.render())