def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                # Thêm điều kiện kiểm tra và chỉ in ra khi điều kiện đúng
                if arrayA[i] < arrayB[j]:
                    print(str(arrayA[i]) + "," + str(arrayB[j]))
                    break  # Dừng vòng lặp k nếu điều kiện đúng

# Example usage:
arrayA = [1, 3, 5]
arrayB = [2, 4, 6]
printUnorderedPairs(arrayA, arrayB)
