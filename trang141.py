def rotate_matrix(matrix):
    n = len(matrix)

    # Xoay từ vị trí (0,0) đến (n-1,n-1)
    for layer in range(n // 2):
        first, last = layer, n - 1 - layer
        for i in range(first, last):
            offset = i - first

            # Lưu giữ giá trị của góc trên bên phải
            top = matrix[first][i]

            # Sao chép giá trị của góc trái dưới vào góc trên bên phải
            matrix[first][i] = matrix[last - offset][first]

            # Sao chép giá trị của góc trái trên vào góc trái dưới
            matrix[last - offset][first] = matrix[last][last - offset]

            # Sao chép giá trị của góc phải trên vào góc trái trên
            matrix[last][last - offset] = matrix[i][last]

            # Sao chép giá trị của góc phải dưới vào góc phải trên
            matrix[i][last] = top

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_matrix(matrix)

# In ra ma trận sau khi xoay
for row in matrix:
    print(row)
