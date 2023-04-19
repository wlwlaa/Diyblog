from django.contrib import admin
from .models import Author, Post, Comment, User


admin.site.register(Author)

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_of_post')
    inlines = [CommentInline]
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('shorted_comment_text', 'author', 'post', 'time_of_comment')

    @admin.display(description='Text')
    def shorted_comment_text(self, obj):
        return obj.comment_text[:76]

    list_filter = ('time_of_comment', 'author')
