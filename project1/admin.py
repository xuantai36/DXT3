from django.contrib import admin
from .models import HANGHOA,KHO,KHOHANGHOA
# Register your models here.
class KHOHANGHOAAdmin(admin.ModelAdmin):
    list_display = ('HangHoa','Kho','SoLuong')
    list_filter = ('Kho','SoLuong')
admin.site.register(HANGHOA)
admin.site.register(KHO)
admin.site.register(KHOHANGHOA,KHOHANGHOAAdmin)