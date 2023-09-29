from django.contrib import admin
from .models import Book, Comment


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "status", "author", "price", "truncate_description"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "book", "truncate_comment", "datetime_created", )

    def truncate_comment(self, obj):
        return obj.text[:30] + "..." if len(obj.text) > 30 else obj.text
    truncate_comment.short_description = "text"

