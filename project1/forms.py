from django import forms
from .models import HANGHOA, KHOHANGHOA

class HangHoaForm(forms.ModelForm):
    SoLuong = forms.IntegerField(required=False, label="Số lượng")

    class Meta:
        model = HANGHOA
        fields = ['Ten', 'MoTa', 'DonViTinh', 'Kho','SoLuong']


