from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # path('detail/<slug:slug>', views.detail, name='detail'),
     path('detail/<slug:slug>', views.Dwtail_Post_View.as_view(), name='detail'),
     path('all_post',views.All_Post.as_view(),name='all_post'),
     path('category_detail/<int:pk>', views.category_detail, name='category_detail'),
     path('serch/', views.serch_post, name='serch'),
    path('contact_us/', views.Cuntact_us_View.as_view(), name='contact_us'),
 ]

