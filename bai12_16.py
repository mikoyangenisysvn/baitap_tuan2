
my_array = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 5]


element_to_check = int(input("Nhập phần tử cần kiểm tra số lần xuất hiện: "))


occurrences = my_array.count(element_to_check)


print(f"Số lần xuất hiện của phần tử {element_to_check} trong mảng là: {occurrences}")
