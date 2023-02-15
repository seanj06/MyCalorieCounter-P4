from django.urls import path
from main.views import home, food_search


urlpatterns = [
    path("", home, name="home"),
    path("food/", food_search, name="food_search"),
    path("profile/", food_list_view, name="food_list"),
    ]