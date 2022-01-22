from django.urls import path

from jquery.views import IndexView, ListView, get_username, username_exists, get_form, get_username

app_name = 'jquery'

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('list/', ListView.as_view(), name='list'),
    path('ajax/', get_form, name='ajax'),
    path('exists/', get_username, name='exists'),
]
