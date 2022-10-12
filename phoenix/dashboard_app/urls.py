from django.urls import path
from phoenix.dashboard_app import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
]
