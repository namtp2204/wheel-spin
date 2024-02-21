# Trong views.py
from django.shortcuts import render, redirect
from .forms import SpinCodeForm
from .models import SpinCode, UsedSpinCode

def spin_form(request):
    if request.method == 'POST':
        form = SpinCodeForm(request.POST)
        spin_code = request.POST.get('code', '')
        if spin_code:
            # Kiểm tra xem spin_code đã được sử dụng trước đó chưa
            if UsedSpinCode.objects.filter(code=spin_code).exists():
                # Nếu spin_code đã được sử dụng, hiển thị thông báo lỗi
                form.add_error('code', 'Spin code đã được sử dụng')
            elif SpinCode.objects.filter(code=spin_code).exists():
                # Nếu spin_code hợp lệ và chưa được sử dụng, lưu vào cơ sở dữ liệu mới và render đến spin_wheel.html
                UsedSpinCode.objects.create(code=spin_code)
                return render(request, 'spin/spin_wheel.html', {'spin_code': spin_code})
        #     else:
        #         # Nếu spin_code không tồn tại trong cơ sở dữ liệu, hiển thị thông báo lỗi
        #         form.add_error('code', 'Spin code không hợp lệ')
        # if form.is_valid():
        #     form.save()
        #     # Redirect hoặc thực hiện các thao tác khác
        #     return redirect('some-url')
    else:
        form = SpinCodeForm()
    return render(request, 'spin/spin_form.html', {'form': form})