from django.urls import path
from phoenix.user_app import views

urlpatterns = [
    path('',views.user,name='user'),
]
