from django.shortcuts import render
from django import forms

# Create your views here.
class Newtaskform(forms.Form):
    task = forms.CharField(label="Task field")
    #phone = forms.IntegerField(label="phone", min_value="10", max_value="12")



tasks = ["buy groceries", "watch football", "visit a friend" ]
def energy(request):
    return render(request,"tasks.html",{
        "tasks": tasks
    })

def add(request):
    if request.method == "POST":
        form = Newtaskform(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tasks.append(task)
        else:
            return render(request, "add.html",{
                "form": form
            })


    return render(request,"add.html",{
        "form":Newtaskform()
    })
class anothertask(forms.Form):
    task = forms.CharField(label="Email")

def ongeza(request):
    return render(request,("ongeza.html"),{
        "fm":anothertask
    })