def twoSum(nums, target):
    # Tạo một từ điển để lưu trữ giá trị và chỉ số của các phần tử đã xét qua
    num_dict = {}

    # Duyệt qua từng phần tử trong mảng nums
    for i, num in enumerate(nums):
        # Tính toán giá trị cần tìm kiếm để có tổng bằng target
        complement = target - num

        # Kiểm tra xem giá trị cần tìm kiếm đã xuất hiện trong từ điển chưa
        if complement in num_dict:
            # Nếu có, trả về chỉ số của hai phần tử cùng với giá trị cần tìm kiếm
            return [num_dict[complement], i]
        else:
            # Nếu không, thêm giá trị hiện tại và chỉ số vào từ điển
            num_dict[num] = i

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)
