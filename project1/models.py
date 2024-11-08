from django.db import models

# Create your models here.
class KHO(models.Model):
    Ten = models.CharField(max_length=100)
    DiaChi= models.CharField(max_length=255)
    def __str__(self):
        return self.Ten
class HANGHOA(models.Model):
    Ten = models.CharField(max_length=200)
    MoTa= models.TextField(blank=True)
    class Donvitinh(models.TextChoices):
        Kg = 'Kg','Kilogram',
        Cai = 'Cai','Cái'
        Chai = 'Chai','Chai'
        Hop = 'Hop','Hộp'
    DonViTinh= models.CharField(max_length=10,choices=Donvitinh.choices)
    Kho= models.ManyToManyField(KHO,through='KHOHANGHOA')
    def __str__(self):
        return self.Ten
class KHOHANGHOA(models.Model):
    HangHoa = models.ForeignKey(HANGHOA,on_delete=models.CASCADE)
    Kho= models.ForeignKey(KHO,on_delete=models.CASCADE)
    SoLuong = models.IntegerField()
    def __str__(self):
        return '{}-{}'.format(self.Kho,self.HangHoa)

