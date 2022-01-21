from django.urls import path

from jquery.views import IndexView, ListView, AjaxView

app_name = 'jquery'

urlpatterns = [
	path('index/', IndexView.as_view(), name='index'),
	path('list/', ListView.as_view(), name='list'),
	path('ajax/', AjaxView.as_view(), name='ajax_view'),
]