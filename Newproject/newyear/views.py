import datetime

from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def func(request):
    now = datetime.datetime
    return render(request, "christmas.html", {
        "new": now.month == 1 and now.day == 1
    })





