from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Image) 
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Film)