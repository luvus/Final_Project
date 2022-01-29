from pipes import Template
from re import template
from django.shortcuts import render
from django.views.generic import TemplateView

class home_index(TemplateView):
    template_name = "home_index.html"