from django.shortcuts import render, get_object_or_404
from django.views import generic, view
from .models import Food

# Create your views here.


class FoodList(generic.ListView):
    model = Food
    template_name = 'base.html'
