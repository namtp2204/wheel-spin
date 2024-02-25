# Sử dụng Python làm base image
FROM python:3.11.2

# Thiết lập biến môi trường
ENV PYTHONUNBUFFERED 1

# Tạo thư mục làm việc và thiết lập thư mục làm việc mặc định cho container
WORKDIR /app

# Copy tệp requirements.txt vào thư mục làm việc của container
COPY requirements.txt /app

# Cài đặt các phụ thuộc Python từ tệp requirements.txt
RUN pip install -r requirements.txt

# Copy toàn bộ mã nguồn của dự án vào thư mục làm việc của container
COPY . /app

# Chạy lệnh migrate để áp dụng các thay đổi cơ sở dữ liệu
RUN python manage.py migrate

# Expose cổng 8000 để có thể truy cập vào ứng dụng Django
EXPOSE 8000

# Khởi động máy chủ Django bằng lệnh runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
