from django.urls import path

from ajax.views import CarDetailView, CarFormView, IndexView, CarUpdateView, delete


app_name = 'ajax'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('form/', CarFormView.as_view(), name='form'),
    path('detail/<int:pk>', CarDetailView.as_view(), name='detail'),
    path('update/<int:pk>', CarUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', delete, name='delete'),
]
