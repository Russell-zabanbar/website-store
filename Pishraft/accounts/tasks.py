from celery import shared_task
from datetime import datetime, timedelta
from accounts.models import Otp_Code
import pytz


@shared_task
def expired_otpcode():
    expired_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    Otp_Code.objects.filter(created__lt=expired_time).delete()