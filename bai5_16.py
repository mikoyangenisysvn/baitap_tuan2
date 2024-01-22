# Mảng mẫu
my_array = [1, 2, 3, 4, 5]
print("Mảng ban đầu:", my_array)
# Mảng để mở rộng (extend)
extension_array = [6, 7, 8]

# Mở rộng mảng bằng cách thêm từng phần tử của mảng mở rộng vào cuối mảng chính
for element in extension_array:
    my_array.append(element)

# Hiển thị mảng đã được mở rộng
print("Mảng đã được mở rộng:", my_array)
