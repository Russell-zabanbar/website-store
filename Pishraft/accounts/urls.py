from django.urls import path 
from accounts import views
app_name = 'accounts'
urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('verify/',views.UserVerifyCodeView.as_view(), name='verify_code'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
]

