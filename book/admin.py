from django.contrib import admin
from .models import Book, BookContent, BookRevision


class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book


class BookRevisionAdmin(admin.ModelAdmin):
    class Meta:
        model = BookRevision


class BookContentAdmin(admin.ModelAdmin):
    class Meta:
        model = BookContent


admin.site.register(Book, BookAdmin)
admin.site.register(BookRevision, BookRevisionAdmin)
admin.site.register(BookContent, BookContentAdmin)
