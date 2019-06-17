from django.contrib import admin

# Register your models here.
from .models import UserOperation,UserReturnBook
class UserOperationAdmin(admin.ModelAdmin):
    list_display = ['name', 'book_name',  'day']
    list_display_links = ['name', 'book_name', 'day']
    list_filter = ['day']
    search_fields = ['name', 'book_name']
admin.site.register(UserOperation,UserOperationAdmin)
class UserReturnBookAdmin(admin.ModelAdmin):
    list_display = ['uname','book_name','day','backtime']
    def uname(self, obj):
        return obj.borrow.name.name
    uname.short_description = "用户名"
    def book_name(self, obj):
        return obj.borrow.book_name.name
    book_name.short_description = "书名"
    def day(self,obj):
        return obj.borrow.day
    day.hort_description = "借书时间"
    list_display_links = ['uname','book_name','day','backtime']
admin.site.register(UserReturnBook,UserReturnBookAdmin)