

from django.urls import path
from . import views

urlpatterns = [
        path('', views.home),
        path('gpd_page/', views.gpd_page),
        path('info/', views.info),
        path('gpd_employee/', views.gpd_employee),
        path('gpd_manager/', views.gpd_manager),
    ]