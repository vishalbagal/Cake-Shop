from django.contrib import admin
from cakeapp.models import Cake

# Register your models here.
class CakeAdmin(admin.ModelAdmin):
    list_display=['id','name','price','detail','cat','is_active']
    list_filter=['cat','is_active']


admin.site.register(Cake,CakeAdmin)