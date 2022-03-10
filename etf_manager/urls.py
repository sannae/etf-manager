from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('etfs/', views.etf_list.as_view(), name='etf_list'),
    path('etf/<str:pk>/', views.etf_detail.as_view(), name='etf_detail'),
]
