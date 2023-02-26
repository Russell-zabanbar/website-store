from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.managers import UserManager
class User(AbstractBaseUser):
    phone_number = models.CharField(max_length=11,unique=True)
    full_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    addresses = models.TextField()
    store_number = models.CharField(max_length=11,unique=True,default='new column')
    avatar = models.ImageField()

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']
    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self,perm,obj=None):
        return True


    def has_module_perms(self,app_label):
        return True


     

class Otp_Code(models.Model):
	phone_number = models.CharField(max_length=11,unique=True)
	code = models.PositiveIntegerField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.phone_number} - {self.code} - {self.created}'
        