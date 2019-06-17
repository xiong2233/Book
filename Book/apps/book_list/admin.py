from django.contrib import admin

# Register your models here.
from .models import BookList,BookCategory

admin.site.register(BookCategory)
# admin.site.register(BookList)

class BookListAdmin(admin.ModelAdmin):
    list_display=['name','num','price']
    list_display_link = ['name','num','price']
    list_filter = ['num','price']
    search_fields = ['name']
admin.site.register(BookList,BookListAdmin)


