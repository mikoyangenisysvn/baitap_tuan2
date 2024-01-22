
input_str = input("Nhập chuỗi cần đảo ngược: ")


reversed_str = ""


for char in input_str:
    reversed_str = char + reversed_str


print("Chuỗi đảo ngược là:", reversed_str)
