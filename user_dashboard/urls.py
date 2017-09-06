from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace='users')),
    url(r'^main/', include('apps.main_app.urls', namespace='main')),
]
