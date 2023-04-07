from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(service)
# admin.site.register(Admin)
# admin.site.register(Doctor)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(Appointment)
admin.site.register(report)
