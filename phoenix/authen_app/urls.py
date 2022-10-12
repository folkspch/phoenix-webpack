from django.urls import path
from phoenix.authen_app import views

urlpatterns = [
    path('',views.authen,name='authen'),
]
