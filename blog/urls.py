from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    # path('detail/<slug:slug>', views.detail, name='detail'),
     path('detail/<slug:slug>', views.Detail_Post_View.as_view(), name='detail'),
     path('all_post',views.All_Post.as_view(),name='all_post'),
     path('category_detail/<int:pk>', views.category_detail, name='category_detail'),
     path('serch/', views.serch_post, name='serch'),
     path('contact_us/', views.Cuntact_us_View.as_view(), name='contact_us'),
    # path('<slug:slug>/<int:pk>', views.like_post, name='like'),
     path('listpostApi', views.ListPost_Api.as_view(), name='listpostApi'),
     path('detailpostApi/<int:pk>', views.detailpost_Api.as_view(), name='detailpostApi'),
     path('add', views.addpostApi.as_view()),
     path('update/<int:pk>', views.update_Api_view.as_view(), name='update'),
 ]

