from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
     path('detail/<slug:slug>', views.detail, name='detail'),
     path('all_post',views.all_post,name='all_post'),
     path('category_detail/<int:pk>', views.category_detail, name='category_detail'),
     path('serch/', views.serch_post, name='serch'),
 ]

