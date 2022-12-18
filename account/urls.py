from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('edit_information_user/<int:pk>', views.Edit_information.as_view(), name='edit'),
    path('delete_user/<int:pk>', views.Delete_User.as_view(), name='delete'),
]