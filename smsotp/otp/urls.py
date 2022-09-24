from django.urls import path
from . import views

app_name = 'otp'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.RegisterNumber.as_view(), name='register_number'),
    path('verify/', views.VerifyCode.as_view(), name='verify_code'),

]
