from django.shortcuts import render
from django.views import View
from .forms import RegisterNumberForm


class HomeView(View):

    def get(self, request):
        return render(request, 'otp/home.html')


class RegisterNumber(View):
    def get(self, request):
        form = RegisterNumberForm
        return render(request, 'otp/register_number.html', {'form': form})

