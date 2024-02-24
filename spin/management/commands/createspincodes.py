import string
import random
from django.core.management.base import BaseCommand
from spin.models import SpinCode

class Command(BaseCommand):
    help = 'Create spin codes and save them to the database'

    def handle(self, *args, **kwargs):
        number_of_codes = 100  # Số lượng spin codes bạn muốn tạo

        # Xóa tất cả các spin codes cũ trước khi tạo mới (nếu cần)
        SpinCode.objects.all().delete()

        # Tạo và lưu các spin codes mới vào cơ sở dữ liệu
        for _ in range(number_of_codes):
            code = self.generate_spin_code()
            SpinCode.objects.create(code=code)
            self.stdout.write(self.style.SUCCESS(f'Successfully created spin code: {code}'))

    def generate_spin_code(self):
        lowercase_letters = string.ascii_lowercase  # Chữ cái viết thường
        uppercase_letters = string.ascii_uppercase  # Chữ cái viết hoa
        digits = string.digits  # Số

        # Chọn một chữ cái viết thường ngẫu nhiên
        lowercase = random.choice(lowercase_letters)
        # Chọn hai chữ cái viết hoa ngẫu nhiên
        uppercase = ''.join(random.choices(uppercase_letters, k=2))
        # Chọn một số ngẫu nhiên
        number = random.choice(digits)

        # Tạo danh sách ký tự từ các loại ký tự trên
        characters = list(lowercase + uppercase)

        # Thêm một số ngẫu nhiên vào danh sách ký tự
        characters.append(number)

        # Xáo trộn thứ tự các ký tự
        random.shuffle(characters)

        # Tạo chuỗi ngẫu nhiên có 8 ký tự từ danh sách các ký tự
        code = ''.join(random.choice(characters) for _ in range(10))
        return code
