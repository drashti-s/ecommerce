from django.shortcuts import render,redirect

# Create your views here.
def indexpage(request):
    return render(request,"showproduct.html")

def manageproduct(request):
    return render(request,"manageproduct.html")

def addproduct(request):
    return render(request,"addproduct.html")

def singleproduct(request):
    return render(request,"singleproduct.html")