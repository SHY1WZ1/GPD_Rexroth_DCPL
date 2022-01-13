"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import *

import numpy as np


def home(request):
    return render(request, 'gpd/dashboard.html')


def gpd_page(request):
    
    return render(request, 'gpd/gpd_page.html')


def info(request):
    return render(request, 'gpd/info.html')

def gpd_employee(request):
    person = Person.objects.get(name='Tetiana')
    context = {
        "data" : [1, 2, 3,4,5],
        "rates":np.round(np.arange(0, 3.1, 0.1),1).tolist(),
    }
    return render(request, 'gpd/gpd_employee.html', {'context':context, 'person':person})

def gpd_manager(request):
    return render(request, 'gpd/manager_dashboard.html')