from django.shortcuts import render, redirect
from django.views import View
from home.models import Product, Category
from accounts.models import User
from home import tasks
from django.contrib import messages
from utils import IsAdminUserMixin

class Normal_Home_View(View):
    def get(self,request):
        return render(request,'normalhome.html')


class HomeView(View):
    def get(self,request,id=None,slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.all()
        
        users = User.objects.filter(pk=id)
        if slug:
            category = Category.objects.get(slug=slug)
            products = products.filter(category=category)  


        return render(request,'home/home.html',{'products':products,'users':users, 'categories':categories})





class ProductDetailesView(View):
    
    def get(self,request,slug):
        products = Product.objects.get(slug=slug)
        
        return render(request,'home/single-product.html',{'products':products})



class BucketHome(IsAdminUserMixin,View):
    def get(self,request):
        get_buckets = tasks.bucket_list_objects()
        return render(request,'bucket.html',{'get_buckets':get_buckets})


class Delete_Obj_Bucket(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.bucket_delete_object.delay(key)
        messages.success(request,'object has bucket in deleted soon','info')        
        return redirect('home:bucket')   
    

class Downlaod_Obj_Bucket(IsAdminUserMixin,View):
    def get(self,request,key):
        tasks.bucket_download_object.delay(key)
        messages.success(request, ' this download objects has soon ','info')
        return redirect('home:bucket')


