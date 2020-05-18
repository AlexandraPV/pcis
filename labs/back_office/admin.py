from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Booking)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Job)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Personal)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Order)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(models.FinishBooking)
class ClientAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Service)
class ClientAdmin(admin.ModelAdmin):
    pass
