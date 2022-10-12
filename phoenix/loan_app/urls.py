from django.urls import path
from phoenix.loan_app import views

urlpatterns = [
    path('',views.loan,name='loan'),
]
