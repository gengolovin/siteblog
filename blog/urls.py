from django.urls import path
from .views import index, get_category

urlpatterns = [
    path('', index, name='index'),
    path('category/<str:slug>', get_category, name='category'),
]
