#Mini-project - thẻ sinh viên
ten = input('Nhập tên:')
msv = input('Nhập mã sinh viên:')
nganh = input('Nhập tên ngành:')
nam_nhap_hoc = int(input('Nhập năm nhập học:'))
if nam_nhap_hoc.isdigit(1):
    nam_tot_nghiep = nam_nhap_hoc + 4
    print(f'{ten} ,{msv}, {nganh}. Khóa học {nam_nhap_hoc} - {nam_tot_nghiep}')
else:
    print('Hãy dùng AI để học!')