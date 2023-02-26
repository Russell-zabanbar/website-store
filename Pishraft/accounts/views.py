from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegisterForm, VerifyCodeForm, UserNameLoginForm 
import random
from accounts.models import User,Otp_Code
from django.contrib import messages
from utils import send_otp_code
from django.urls import reverse


class UserRegisterView(View):
    def get(self,request):
        form = RegisterForm
        return render(request,'accounts/login.html',{'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            user=User.objects.filter(phone_number=form.cleaned_data['phone_number']).exists()
            if user:
                random_code = random.randint(1000,9999)
                send_otp_code(form.cleaned_data['phone_number'], random_code)
                Otp_Code.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
                request.session['user_registration_info'] = {
                    'phone_number':form.cleaned_data['phone_number'],
                }
                messages.success(request,'we sent you a code','success')
                return redirect('accounts:verify_code')    
            else:
                messages.error(request,'you not signin account, pleas regester','warning')
                return render(request,'accounts/login.html',{'form':form})
        return render(request,'accounts/login.html',{'form':form})


class UserVerifyCodeView(View):
    def get(self, request):
        form = VerifyCodeForm
        return render(request,'accounts/otp-verification.html',{'form':form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instanse = Otp_Code.objects.get(phone_number=user_session['phone_number'])
        form = VerifyCodeForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instanse.code:

                user=User.objects.get(phone_number=user_session['phone_number'])
                login(request,user)

                code_instanse.delete()
                return redirect (reverse('home:home' , args=[user.id]))
            else:
                messages.error(request,'this code is wrong','danger')
                return redirect('accounts:verify_code')
        return render(request,'accounts/otp-verification.html',{'form':form})

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:normalhome') 




