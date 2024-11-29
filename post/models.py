from django.db import models

class Visit(models.Model):
    ip_address = models.GenericIPAddressField()  
    visit_date = models.DateField(auto_now_add=True)
