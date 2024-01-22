def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            print(str(array[i]) + "," + str(array[j]))

# Gọi hàm với một mảng
printUnorderedPairs([1, 2, 3])
