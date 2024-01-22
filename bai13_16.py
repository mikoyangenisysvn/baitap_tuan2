from array import array


my_array = array('i', [1, 2, 3, 4, 5])


array_as_string = my_array.tobytes().decode('utf-8')


print("Mảng đã chuyển đổi thành chuỗi:", array_as_string)
