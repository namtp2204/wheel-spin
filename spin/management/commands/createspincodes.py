# trong createspincodes.py

from django.core.management.base import BaseCommand
from spin.models import SpinCode
import random
import string

class Command(BaseCommand):
    help = 'Create spin codes and save them to the database'

    def handle(self, *args, **kwargs):
        number_of_codes = 10  # Số lượng spin codes bạn muốn tạo

        # Xóa tất cả các spin codes cũ trước khi tạo mới (nếu cần)
        SpinCode.objects.all().delete()

        # Tạo và lưu các spin codes mới vào cơ sở dữ liệu
        for _ in range(number_of_codes):
            code = self.generate_spin_code()
            SpinCode.objects.create(code=code)
            self.stdout.write(self.style.SUCCESS(f'Successfully created spin code: {code}'))

    def generate_spin_code(self):
        characters = string.ascii_uppercase + string.digits + string.punctuation  # Chữ cái viết hoa + số + ký tự đặc biệt
        code = ''.join(random.choice(characters) for _ in range(6))  # Tạo chuỗi ngẫu nhiên có 6 ký tự
        return code
