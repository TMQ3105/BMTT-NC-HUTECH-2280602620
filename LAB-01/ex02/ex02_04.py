# Tạo một danh sách rỗng lưu kết quả
danh_sach = []

# Duyệt qua tất cả các số trong đoạn từ 2000 đến 3200
for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        danh_sach.append(str(i))

# In danh sách kết quả, các số cách nhau bởi dấu phẩy
print(','.join(danh_sach))