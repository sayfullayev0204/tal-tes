from django.shortcuts import render
from post.models import Visit
from datetime import date

# Create your views here.
def home(request):
    today_visitors_count = Visit.objects.filter(visit_date=date.today()).count()
    return render(request, 'index.html', {'today_visitors_count': today_visitors_count})

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