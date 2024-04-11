from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def adminsignin(request):
    template = loader.get_template ('adminsignin.html')
    return HttpResponse(template.render())
