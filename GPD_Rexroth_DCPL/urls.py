"""
GPD_Rexroth_DCPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
import gpd.views

# Django processes URL patterns in the order they appear in the array
# Each URL pattern describes the views to which Django routes specific 
# site-relative URLs (that is, the portion that follows https://www.domain.com/). 
# The first entry in urlPatterns that starts with the regular expression ^$ is the routing for the site root, "/". 
# The second entry, ^home$ specifically routes "/home". You can have any number of routings to the same view.
urlpatterns = [
    path('', gpd.views.index, name='home'),
    path('about/', gpd.views.about, name='about'),
    path('home/', gpd.views.index, name='home'),
    path('admin/', admin.site.urls),
]