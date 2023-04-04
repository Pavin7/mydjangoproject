import datetime

from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.
def test(request):
    now = datetime.datetime
    return render(request, "index.html", {
        "new": now.month == 1 and now.day == 1
    })





