from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args,**kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request,"home.html",{})

def about_view(request,*args,**kwargs):
    info={
        "name":"Sid",
        "address":"Baneshwor",
        "mobile":9808877669,
        "list":["a","b","c"]
    }
    return render(request,"about.html",info)