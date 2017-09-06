from django.conf.urls import url
from . import views
app_name = 'main'

urlpatterns = [
    url(r'^dashboard/admin$', views.dashboard_admin, name='dashboard_admin'),
    url(r'^dashboard$', views.dashboard_user, name='dashboard_user'),
    url(r'^user/new$', views.add_user, name='add_user'),
    url(r'^createUser$', views.create_user, name='create_user'),
    url(r'^user/edit/(?P<user_id>\d+)$', views.edit_profile, name='edit_profile'),
    url(r'^user/edit_info/(?P<user_id>\d+)$', views.edit_info, name='edit_info'),
    url(r'^user/change_password/(?P<user_id>\d+)$', views.change_password, name='change_password'),
    url(r'^user/change_description/(?P<user_id>\d+)$', views.change_description, name='change_description'),
    url(r'^user/remove_user/(?P<user_id>\d+)$', views.remove_page, name='remove_page'),
    url(r'^user/delete/(?P<user_id>\d+)$', views.delete_this_user, name='delete_user'),
    url(r'^user/show/(?P<user_id>\d+)$', views.view_user, name='view_user'),
    url(r'^user/add_message/(?P<user_id>\d+)$', views.post_message, name='post_message'),
]
