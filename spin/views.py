from django.shortcuts import render, redirect
from .forms import SpinCodeForm
from .models import SpinCode, UsedSpinCode
from django.contrib import messages 
from django.urls import reverse

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
                return redirect(reverse('spin:spin_wheel', kwargs={'spin_code': spin_code}))
                # return render(request, 'spin/spin_wheel.html', {'spin_code': spin_code})
            else:
                messages.error(request, 'Spin code không hợp lệ')
                return render(request, 'spin/spin_form.html', {'form': form})
    else:
        form = SpinCodeForm()
    return render(request, 'spin/spin_form.html', {'form': form})

def spin_wheel(request, spin_code):
    # Xử lý logic của trang spin_wheel ở đây
    return render(request, 'spin/spin_wheel.html', {'spin_code': spin_code})



def navigation(request):

    return render(request, 'spin/navigation.html')
