from django.urls import path
from home import views


app_name = 'home'
urlpatterns = [
    path('home_page_user/<int:id>/', views.HomeView.as_view(), name='home'),
    path('category/<slug:slug>/', views.HomeView.as_view(), name='home_slug'),
    path('',views.Normal_Home_View.as_view(),name='normalhome'),
    path('bucket/',views.BucketHome.as_view(),name='bucket'),
    path('download_obj_bucket/<str:key>/',views.Downlaod_Obj_Bucket.as_view(),name='download_obj_bucket'),
    path('delete_obj_bucket/<str:key>/',views.Delete_Obj_Bucket.as_view(),name='delete_obj_bucket'),
    path('<slug:slug>/',views.ProductDetailesView.as_view(),name='product'),
    
]
