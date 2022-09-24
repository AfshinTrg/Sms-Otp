from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterNumberForm, VerifyCodeForm
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
            request.session['phone_info'] = {
                'phone_number': cd['phone'],
            }
            messages.success(request, 'we sent you a code', 'success')
            return redirect('otp:verify_code')


class VerifyCode(View):
    def get(self, request):
        form = VerifyCodeForm
        return render(request, 'otp/verify_code.html', {'form': form})

    def post(self, request):
        user_session = request.session['phone_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = VerifyCodeForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                messages.success(request, 'Your code is correct', 'success')
                code_instance.delete()
                return redirect('otp:home')
            else:
                messages.error(request, 'this code is wrong', 'danger')
                return redirect('otp:verify_code')










