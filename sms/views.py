from django.http import HttpResponse
from django.shortcuts import render
from .tasks import send_sms_task


# Create your views here.

def sms_form(request):
    return render(request, 'sms/form.html', {})


def send_sms(request):
    phone_number = request.POST['phone_number']
    message_text = request.POST['message_text']
    print(message_text, phone_number)
    send_sms_task.delay(phone_number, message_text)
    return HttpResponse('ok')
