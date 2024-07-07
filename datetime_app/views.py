from django.shortcuts import render
from datetime import datetime, timedelta

def datetime_view(request):
    current_datetime = datetime.now()
    four_hours_ahead = current_datetime + timedelta(hours=4)
    four_hours_before = current_datetime - timedelta(hours=4)
    
    context = {
        'current_datetime': current_datetime,
        'four_hours_ahead': four_hours_ahead,
        'four_hours_before': four_hours_before,
    }
    
    return render(request, 'datetime_app/datetime.html', context)
# Create your views here.
