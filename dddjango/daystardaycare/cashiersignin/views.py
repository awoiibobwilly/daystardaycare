from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def cashiersignin(request):
    template = loader.get_template ('cashiersignin.html')
    return HttpResponse(template.render())