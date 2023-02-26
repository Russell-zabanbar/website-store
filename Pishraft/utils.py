from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *
from Pishraft import settings

def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_APIKEY)
        params = {
            'sender':'',
            'receptor':phone_number,
            'message':f'{code}کد تایید شما'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)



class IsAdminUserMixin(UserPassesTestMixin):
    def test_func(self):
        user=self.request.user.is_authenticated and self.request.user.is_admin
        if user:
            return user

        else:
            pass