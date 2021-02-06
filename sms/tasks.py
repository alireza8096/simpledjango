from celery import shared_task
from kavenegar import *


@shared_task
def send_sms_task(phone_number, message):
    api = KavenegarAPI('38356357594D45396D4272705072306E386358414830533967516B5437374645736A79356C3862517A50733D')
    params = {'sender': '1000596446', 'receptor': phone_number, 'message': message}
    response = api.sms_send(params)
    return response
