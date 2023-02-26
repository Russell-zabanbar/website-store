from django.shortcuts import render
from django.views import View
from accounts.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

class UserProfileView(LoginRequiredMixin,View):
    def get(self,request,id):
        profile_user=User.objects.filter(pk=id)
        return render(request,'profiles/profile.html',{'profile_user':profile_user})
        