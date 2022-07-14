from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.subs, name='subs'),
    path('add-sub/', views.add_sub, name='add-sub'),
]
