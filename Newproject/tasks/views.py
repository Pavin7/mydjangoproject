from django.shortcuts import render

# Create your views here.
tasks = ["buy groceries", "watch football", "visit a friend" ]
def energy(request):
    return render(request,"tasks.html",{
        "tasks": tasks
    })

def add(request):
    return render(request,"add.html")
