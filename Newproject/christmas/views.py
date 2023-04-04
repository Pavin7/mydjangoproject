from django.shortcuts import render

# Create your views here.

import datetime

# Create your views here.
def test(request):
    now = datetime.datetime
    return render(request, "index.html", {
        "new": now.month == 12 and now.day == 25
    })
