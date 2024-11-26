from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('uzum-ser/', admin.site.urls),
    path('', include('app.urls')),
)

# i18n marshrutini qo'shing
urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n')),  # Tilni sozlash uchun marshrut
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
