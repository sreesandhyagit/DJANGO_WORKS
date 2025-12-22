from django.contrib import admin
from manager.models import Author,Category
# Register your models here.

admin.site.register(Author)

class CategoryAdmin(admin.ModelAdmin):
    list_display=["category"]
    prepopulated_fields={"slug":["category"]}

admin.site.register(Category,CategoryAdmin)
