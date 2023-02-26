from django.urls import path
from profiles import views

app_name = 'user_profiles'

urlpatterns = [
    path('profiles/<int:id>/',views.UserProfileView.as_view(),name='profile'),
]
