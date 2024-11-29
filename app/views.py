from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def jamiyat_tarixi(request):
    return render(request, 'jamiyat/jamiyat_tarixi.html')

def jamiyat_bugun(request):
    return render(request, 'jamiyat/jamiyat_bugun.html')

def raxbar(request):
    return render(request, 'jamiyat/raxbar.html')

def ish(request):
    return render(request, 'jamiyat/ish.html')

def strategiya(request):
    return render(request, 'jamiyat/strategiya.html')

def horij(request):
    return render(request, 'horij/horij.html')