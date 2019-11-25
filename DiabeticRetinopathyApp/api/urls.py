from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('error/', views.error, name='error'),
    path('about/', views.about, name='about'),
    path('index/', views.index, name='index'),
    path('results/<int:FinalValue>', views.results, name='results')
]