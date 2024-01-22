def factorial(n):
    # Kiểm tra nếu n là số âm
    if n < 0:
        return -1
    # Giai thừa của 0 là 1
    elif n == 0:
        return 1
    # Trường hợp n > 0
    else:
        # Gọi đệ quy để tính giai thừa của (n-1)
        return n * factorial(n - 1)

# Example usage:
result = factorial(5)
print(f"The factorial of 5 is: {result}")
