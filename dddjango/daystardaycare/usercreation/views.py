from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def usercreation(request):
    template = loader.get_template ('usercreation.html')
    return HttpResponse(template.render())