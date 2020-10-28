from django.contrib import admin

# Register your models here.
from .models import Customer1,Orders

class Customer1Admin (admin.ModelAdmin):
    list_display = ['name','city','phone']
admin.site.register(Customer1,Customer1Admin)


class OrderAdmin (admin.ModelAdmin):
    list_display = ['customer', 'p_name','p_price']
admin.site.register(Orders,OrderAdmin)