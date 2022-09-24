from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterNumberForm
import random
from .models import OtpCode
from django.contrib import messages
from .utils import send_otp_code


class HomeView(View):

    def get(self, request):
        return render(request, 'otp/home.html')


class RegisterNumber(View):
    def get(self, request):
        form = RegisterNumberForm
        return render(request, 'otp/register_number.html', {'form': form})

    def post(self, request):
        form = RegisterNumberForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            random_code = random.randint(1000, 9999)
            send_otp_code(cd['phone'], random_code)
            OtpCode.objects.create(phone_number=cd['phone'], code=random_code)
            messages.success(request, 'we sent you a code', 'success')
            return redirect('otp:verify_code')


class VerifyCode(View):
    def get(self, request):
        pass

    def post(self, request):
        pass







