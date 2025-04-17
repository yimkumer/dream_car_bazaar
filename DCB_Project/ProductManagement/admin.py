from django.contrib import admin
from .models import *
# Register your models here.

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'is_read', 'created_at','car')
    fields = ('user', 'message', 'is_read', 'created_at','car','source')
    
admin.site.register(CarModel)
admin.site.register(CarVariant)
admin.site.register(CarBrands)
admin.site.register(CarImage)
admin.site.register(CarDetails)
admin.site.register(InsuranceCompany)
admin.site.register(CarViews)
admin.site.register(WishlistCar)
admin.site.register(Insurance)
admin.site.register(Warranty)
admin.site.register(DraftCarDetails)
admin.site.register(Lead)
admin.site.register(Notification, NotificationAdmin)

