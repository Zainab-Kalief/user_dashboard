from django.conf.urls import url
from . import views
app_name = 'users'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signin$', views.sign_in, name='sign_in'),
    url(r'^register$', views.register, name='register'),
    url(r'^registerTest$', views.register_test, name='register_test'),
    url(r'^signIn_test$', views.signIn_test, name='signIn_test'),
]
