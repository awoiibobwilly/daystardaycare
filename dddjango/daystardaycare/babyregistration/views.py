from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def babyregistration(request):
    template = loader.get_template ('babyregistration.html')
    return HttpResponse(template.render())