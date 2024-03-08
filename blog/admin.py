from django.contrib import admin
from blog import models
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    fieldsets = [
        ("Title", {"fields" : ["post_title"]}),
        ("Post contents", {"fields" : ["post_content"]}),
        ("Originally posted", {"fields" : ["created_at"]}),
        ("Last updated", {"fields" : ["updated_at"]}),
        ("Tags", {"fields" : ["post_tags"]})
    ]
    
    list_display = ["post_title", "created_at", "updated_at", "post_draft"]
    list_filter = ["created_at", "updated_at"]

class CommentAdmin(admin.ModelAdmin):
    readonly_fields = ("comment_date",)
    fieldsets = [
        ("Author", {"fields" : ["author"]}),
        ("Email", {"fields" : ["author_mail"]}),
        ("Posted at", {"fields" : ["comment_date"]}),
        ("Contents", {"fields" : ["com_content"]})
    ]

    list_display = ["author", "author_mail", "comment_date"]
    list_filter = ["comment_date"]

admin.site.register(Post, PostAdmin)
admin.site.register(models.Tag, admin.ModelAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.

