from django.urls import path
from .  import  views

urlpatterns = [
    path('', views.home, name='home'),
    path('jamiyat-tarixi/', views.jamiyat_tarixi, name="jamiyat_tarixi"),
    path('jamiyat-bugun/', views.jamiyat_bugun, name="jamiyat_bugun"),
    path('raxbar/', views.raxbar, name="raxbar"),
    path('ish/', views.ish, name="ish"),
    path('strategiya/', views.strategiya, name="strategiya"),
]