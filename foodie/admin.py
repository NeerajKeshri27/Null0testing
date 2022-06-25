from django.contrib import admin
from .models import FoodPlaza
# Register your models here.

class foodAdmin(admin.ModelAdmin):
    list_display = ['id','Dish_def','Item_name','Price','Confectionary']

admin.site.register(FoodPlaza , foodAdmin)