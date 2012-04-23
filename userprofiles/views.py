from django.shortcuts import redirect
from django.contrib.auth import logout


def auth_logout(request):
    logout(request)
    return redirect('home')
