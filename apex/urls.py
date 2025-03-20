from django.urls import path
from .views import legend_list, random_legend, legend_list_api, random_legend_api


urlpatterns = [
    path('', legend_list, name='legend_list'),
    path('random/', random_legend, name='random_legend'),
    path('api/legends/', legend_list_api, name='legend_list_api'),
    path('api/random-legend/', random_legend_api, name='random_legend_api'),
]
