from django.contrib import admin

from django.contrib import admin
from .models import Status, Type, Category, Subcategory, DDSRecord

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(DDSRecord)
