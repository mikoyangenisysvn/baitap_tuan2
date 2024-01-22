from array import array

# Mảng mẫu
my_array = array('i', [1, 2, 3, 4, 5])

# Danh sách để thêm vào mảng
list_to_add = [6, 7, 8]

# Thêm từng phần tử của danh sách vào mảng bằng cách sử dụng vòng lặp
for item in list_to_add:
    my_array.append(item)

# Hiển thị mảng sau khi đã thêm
print("Mảng sau khi đã thêm:", my_array)
