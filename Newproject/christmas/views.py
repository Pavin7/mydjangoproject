from django.shortcuts import render

# Create your views here.

import datetime

# Create your views here.
def funny(request):
    now = datetime.datetime
    return render(request, "christmas.html", {
        "new": now.month == 12 and now.day == 25
    })
