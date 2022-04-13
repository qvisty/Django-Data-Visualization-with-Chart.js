from django.contrib import admin
from .models import CountryData, Freetime, Employee

# Register your models here.
admin.site.register(CountryData)
admin.site.register(Freetime)
admin.site.register(Employee)
