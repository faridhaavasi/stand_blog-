from django.contrib import admin
from . models import Post, Category, Comment, Ticket
# Register your models here.

@admin.register(Post)
class Post_admin(admin.ModelAdmin):

    list_display = ('title', 'created', 'status', 'show_post_category', 'show_img')
    list_filter = ('title', 'created')
    search_fields = ('title', 'created')
    list_editable = ('status',)



admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ticket)
