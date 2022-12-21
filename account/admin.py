from django.contrib import admin
from .models import Profile
# Register your models here.
@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
    list_display = ('user', 'melicode')
    list_filter = ('user', 'melicode')
    search_fields = ('user', 'melicode')



#admin.site.register(Profile, Profile_Admin)

