from datetime import date
from .models import Visit

class RecordVisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Foydalanuvchi IP manzilini olish
        ip = self.get_client_ip(request)
        if ip:
            # Bugungi tashriflar mavjudligini tekshirish
            if not Visit.objects.filter(ip_address=ip, visit_date=date.today()).exists():
                Visit.objects.create(ip_address=ip)  # Yangi tashrifni yozib qo'yamiz
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
