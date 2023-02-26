from django import forms 
from accounts.models import User, Otp_Code
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('phone_number','full_name','last_login','is_admin','is_active','avatar','store_number','addresses')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1']:
            raise ValidationError('not match password field')
        return cd['password1']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\">this form</a>.")

	class Meta:
		model = User
		fields = ('phone_number', 'full_name', 'password','last_login','addresses','store_number','avatar')


class RegisterForm(forms.Form):

	phone_number = forms.CharField(widget=forms.NumberInput(
	attrs={'class':'form-control',
	'placeholder':'شماره تلفن'}),max_length=11,label='')


	def clean_phone_number(self):
		phone = self.cleaned_data['phone_number']
		otp = Otp_Code.objects.filter(phone_number=phone)
		if otp:
			otp.delete()
		return phone
class VerifyCodeForm(forms.Form):
	code = forms.IntegerField(widget=forms.NumberInput(
		attrs={'class':'form-control'}),label='')




class UserNameLoginForm(forms.Form):
		full_name = forms.CharField(widget=forms.TextInput(
	 	attrs={'class':'form-control',
	    'placeholder':'نام و نام خوانوادگی'}),max_length=30,label='')
