
my_array = [10, 20, 30, 40, 50]


index = int(input("Nhập chỉ mục của phần tử bạn muốn lấy: "))


if 0 <= index < len(my_array):
   
    element = my_array[index]
    print(f"Phần tử ở chỉ mục {index} là: {element}")
else:
    print("Chỉ mục không hợp lệ")
