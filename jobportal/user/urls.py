
from django.urls import path
from .views import *
# from apis.views import *

app_name = 'account'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/',register_view,name='register'),
    path('user_update/<int:id>/',user_update_view,name='user_update'),  
    path('list/',user_list_view,name='list'),    
    path('detail/<int:id>/',user_detail_view,name='detail'),

    path('add_group',create_group,name='add-group'),
    # path('update_group/<int:id>/',update_group,name='update-group'),
    path('group_list',group_list_view,name='group-list'),


    path('signin/',signin_view,name='signin'),
    path('profile/<int:id>/',user_detail_view,name='profile'),
    path('update/<int:id>/',update_view,name='update'),
]