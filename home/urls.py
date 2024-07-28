from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name="home_page"),
    path('add_data/', add_data_page, name="add_data_page"),
    path('view_data/', view_data_page, name="view_data_page")
]