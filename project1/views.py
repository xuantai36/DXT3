from django.shortcuts import render, get_object_or_404,redirect

from .forms import HangHoaForm
from .models import HANGHOA, KHOHANGHOA
from django.contrib import messages


# Create your views here.
def suahanghoa(request, idhanghoa=None):
    if idhanghoa:
        hanghoa = get_object_or_404(HANGHOA, id=idhanghoa)
        title = "SỬA THÔNG TIN MẶT HÀNG"
        nut = 'Update'
    else:
        hanghoa = None
        title = 'THÊM MỚI MẶT HÀNG'
        nut = 'Create'

    if request.method == "POST":
        form = HangHoaForm(request.POST, instance=hanghoa)
        if form.is_valid():
            update_hanghoa = form.save(commit=False)  # Lưu HANGHOA nhưng không commit vào DB
            so_luong = form.cleaned_data['SoLuong']  # Số lượng từ form
            ds_kho = form.cleaned_data['Kho']        # Lấy danh sách kho từ form

            update_hanghoa.save()  # Lưu HANGHOA vào DB

            # Nếu tạo mới (hanghoa=None), tạo bản ghi mới trong KHOHANGHOA cho mỗi kho
            if hanghoa is None:
                for kho in ds_kho:
                    KHOHANGHOA.objects.create(
                        HangHoa=update_hanghoa,
                        Kho=kho,
                        SoLuong=so_luong
                    )
                messages.success(request, f"Thêm mặt hàng \"{update_hanghoa}\" thành công")
            else:
                # Nếu đang cập nhật, sửa hoặc tạo mới KHOHANGHOA cho mỗi kho
                for kho in ds_kho:
                    KHOHANGHOA.objects.update_or_create(
                        HangHoa=update_hanghoa,
                        Kho=kho,
                        defaults={'SoLuong': so_luong}
                    )
                messages.success(request, f"Các thông tin điều chỉnh của mặt hàng \"{update_hanghoa}\" đã được lưu lại.")

            return redirect('dshanghoa')
    else:
        # Nếu là GET, tạo form với instance và điền sẵn Số lượng nếu có
        form = HangHoaForm(instance=hanghoa)

    return render(request, 'suahanghoa.html', {'hanghoa': hanghoa, 'title': title, 'nut': nut, 'form': form, 'messages': messages})




def dshanghoa(request):
    hanghoaa= KHOHANGHOA.objects.all()
    return render(request,'dshanghoa.html',{'hanghoaa':hanghoaa})