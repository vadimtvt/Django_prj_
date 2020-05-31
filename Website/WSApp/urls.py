from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('description/<int:id_art>', description),
    path('add-post', add_post.as_view(), name='add'),
    path('update-post/<int:pk>', update_post.as_view(), name='update'),
    path('del-post/<int:pk>', del_post.as_view(), name='del'),
    path('login-page', MyLoginView.as_view(), name='login'),
    path('auth-page', MyAuthView.as_view(), name='auth'),
    path('logout-page', MyLogOutView.as_view(), name='logout'),
]
