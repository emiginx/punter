from django.contrib import admin
from .models import *

class PredictionAdmin(admin.ModelAdmin):
    search_fields = ['booking_code','description']
    list_display = ['booking_code','booking_company','description','category','status','created_at']
    list_filter = ['category','created_at','status']

class PredictionItemInline(admin.TabularInline):
    model = Prediction
    raw_id_fields = ['category']

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PredictionItemInline]

# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Prediction,PredictionAdmin)