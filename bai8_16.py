
input_str = input("Nhập mảng các số, cách nhau bằng dấu phẩy (ví dụ: 1,2,3): ")


try:
    my_array = [int(x) for x in input_str.split(',')]
except ValueError:
    print("Nhập không hợp lệ. Vui lòng nhập mảng các số.")


if my_array:
    
    my_array.pop()

    
    print("Mảng sau khi loại bỏ phần tử cuối cùng:", my_array)
else:
    print("Mảng trống.")
