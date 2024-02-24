from django.shortcuts import render, redirect
from .forms import SpinCodeForm
from .models import SpinCode, UsedSpinCode
from django.contrib import messages 

def spin_form(request):
    if request.method == 'POST':
        form = SpinCodeForm(request.POST)
        spin_code = request.POST.get('code', '')
        if spin_code:
            if UsedSpinCode.objects.filter(code=spin_code).exists():
                messages.error(request, 'Spin code đã được sử dụng')
                return render(request, 'spin/spin_form.html', {'form': form})
            elif SpinCode.objects.filter(code=spin_code).exists():
                UsedSpinCode.objects.create(code=spin_code)
                return render(request, 'spin/spin_wheel.html', {'spin_code': spin_code})
            else:
                messages.error(request, 'Spin code không hợp lệ')
                return render(request, 'spin/spin_form.html', {'form': form})
    else:
        form = SpinCodeForm()
    return render(request, 'spin/spin_form.html', {'form': form})
