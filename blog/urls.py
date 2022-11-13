from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
     path('detail/<slug:slug>', views.detail, name='detail'),
    path('all_post',views.all_post,name='all_post'),
 ]

