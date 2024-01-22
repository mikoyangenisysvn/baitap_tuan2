# Mảng mẫu
my_array = [1, 2, 3, 4, 5]

# Giá trị cần xóa
value_to_remove = 3

# Xóa giá trị từ mảng bằng cách sử dụng phương thức remove()
if value_to_remove in my_array:
    my_array.remove(value_to_remove)
    print(f"Giá trị {value_to_remove} đã được xóa từ mảng.")
else:
    print(f"Giá trị {value_to_remove} không tồn tại trong mảng.")

# Hiển thị mảng sau khi đã xóa
print("Mảng sau khi đã xóa:", my_array)
