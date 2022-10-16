from django.urls import path
from phoenix.authen_app import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('2fa/',views.twofa,name='2fa'),
]
