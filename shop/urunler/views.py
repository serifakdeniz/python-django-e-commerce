from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import kategoriler,Markalar,Urunler



# Create your views here.
def anasayfa(request):
    urunler=Urunler.objects.all()
    return render(request,"base.html",{"urunler":urunler})

