from django.contrib import admin

# Register your models here.
from .models import UserInfo,Administrator

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['name','email','money']
    list_display_links = ['name','email','money']
    search_fields = ['name']
admin.site.register(UserInfo,UserInfoAdmin)
admin.site.register(Administrator)