from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('combos', views.get_combo_page, name='combo_page'),
]