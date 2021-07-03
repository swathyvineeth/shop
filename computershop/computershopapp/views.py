from django.shortcuts import render
from .models import product

# Create your views here.

def host(request):
    obj=product.objects.all()
    return render(request,"index.html",{'product':obj})

