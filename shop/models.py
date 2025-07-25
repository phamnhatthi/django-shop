from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)  # Tên sản phẩm, kiểu chuỗi, tối đa 200 ký tự
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá, kiểu số thập phân, tối đa 10 số, 2 số sau dấu phẩy
    description = models.TextField(blank=True)  # Mô tả, có thể để trống
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo, tự động lấy thời gian hiện tại khi tạo mới
    image = models.ImageField(upload_to='products/',blank=True, null=True)
    def __str__(self):
        return self.name  # Hiển thị tên sản phẩm khi in đối tượng Product
