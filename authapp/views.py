from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout




# Create your views here.
def suview(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/a1/lgv/")

    return render(request,"authapp/signup.html",{"form":form})


def lgview(request):
    if request.method =="POST":
        u = request.POST.get("unm")
        p = request.POST.get("pw")
        user = authenticate(username=u,password=p)
        if user!= None:
            login(request,user)
            return redirect("/a1/sv")
    return render(request,"authapp/login.html",{})

def loview(request):
    logout(request)
    return redirect("/a2/lgv/")

