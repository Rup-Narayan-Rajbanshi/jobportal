
from django.urls import path
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserListAPIView,
    UserDetailAPIView,
    UserUpdateAPIView,
    UserDeleteAPIView,
    )
# from apis.views import *

app_name = 'account-api'

urlpatterns = [
    path('create/',UserCreateAPIView.as_view(),name='create'),
    path('login/',UserLoginAPIView.as_view(),name='login'),
    path('list/',UserListAPIView.as_view(),name='list'),
    path('<str:username>/',UserDetailAPIView.as_view(),name='detail'),
    path('<str:username>/update/',UserUpdateAPIView.as_view(),name='update'),
    path('<str:username>/delete/',UserDeleteAPIView.as_view(),name='delete'),


    # path('login/', login_view, name='login'),
    # path('logout/', logout_view, name='logout'),
    # path('register/',register_view,name='register'),
    # path('user_update/<int:id>/',user_update_view,name='user_update'),  
        
    # path('detail/<int:id>/',user_detail_view,name='detail'),

    # path('add_group',create_group,name='add-group'),
    # # path('update_group/<int:id>/',update_group,name='update-group'),
    # path('group_list',group_list_view,name='group-list'),


    # path('signin/',signin_view,name='signin'),
    # path('profile/<int:id>/',user_detail_view,name='profile'),
    # path('update/<int:id>/',update_view,name='update'),
]