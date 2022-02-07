from django.urls import path

from javascript.views import IndexView


app_name = 'javascript'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]