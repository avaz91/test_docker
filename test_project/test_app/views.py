from django.shortcuts import render
from django.views.generic import CreateView
from .models import Test

class TestView(CreateView):
    model= Test
    fields="name", "last_name"
    template_name="test.html"
  