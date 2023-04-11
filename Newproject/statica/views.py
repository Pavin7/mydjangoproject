from django.shortcuts import render

# Create your views here.
def force(request):
    return render(request, "static.html")


