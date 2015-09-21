from django.contrib import admin
from printy.models import Page, PostIt, PrintPage, PostItModel
# Register your models here.


class PostInline(admin.TabularInline):
    model = PostIt


class PrintPageAdmin(admin.ModelAdmin):
    inlines = [
        PostInline
    ]

admin.site.register(Page)
admin.site.register(PostIt)
admin.site.register(PostItModel)
admin.site.register(PrintPage, PrintPageAdmin)
