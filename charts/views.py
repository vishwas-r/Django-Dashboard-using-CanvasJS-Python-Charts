from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    area_data = [
        { "label": "Jan", "y": 10000 },
        { "label": "Feb", "y": 30162 },
        { "label": "Mar", "y": 26263 },
        { "label": "Apr", "y": 18394 },
        { "label": "May", "y": 18287 },
        { "label": "Jun", "y": 28682 },
        { "label": "Jul", "y": 31274 },
        { "label": "Aug", "y": 33259 },
        { "label": "Sep", "y": 25849 },
        { "label": "Oct", "y": 24159 },
        { "label": "Nov", "y": 32651 },
        { "label": "Dec", "y": 31984 }
    ]
    column_data = [
        { "label": "January", "y": 42150 },
        { "label": "February", "y": 53120 },
        { "label": "March", "y": 62510 },
        { "label": "April", "y": 78410 },
        { "label": "May", "y": 98210 },
        { "label": "June", "y": 149840 }
    ]
    pie_data = [
        { "y": 12.21, "name": "Blue", "color": "#007bff" },
        { "y": 15.58, "name": "Red", "color": "#dc3545" },
        { "y": 11.25, "name": "Yellow", "color": "#ffea00" },
        { "y": 8.32, "name": "Green", "color": "#28a745" }
    ]
    return render(request, 'index.html', { "area_data" : area_data, "column_data": column_data, "pie_data": pie_data })