from django.contrib import admin
from . models import Post, Category, Comment, Ticket
# Register your models here.

@admin.register(Post)
class Post_admin(admin.ModelAdmin):

    list_display = ('title', 'created', 'status', 'show_post_category', 'show_img')
    list_filter = ('title', 'created')
    search_fields = ('title', 'created')
    list_editable = ('status',)
    actions = ['make_published']

    @admin.action(description='نتشر کردن آیتم های انتخابی')
    def make_published(self, request, queryset):
        queryset.update(status='p')




admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ticket)
