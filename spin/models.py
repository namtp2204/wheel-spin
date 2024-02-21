from django.db import models

class SpinCode(models.Model):
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.code

class UsedSpinCode(models.Model):
    code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.code
#git

# class CustomerInfo(models.Model):
#     facebook_name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     spin_code = models.ForeignKey(SpinCode, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.facebook_name
