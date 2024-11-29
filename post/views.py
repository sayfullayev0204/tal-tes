from datetime import date
from .models import Visit

def get_daily_visitors_count():
    today = date.today()
    return Visit.objects.filter(visit_date=today).count()
