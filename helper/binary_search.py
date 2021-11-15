def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        elif arr[m] > x:
            r = m - 1
        else:
            return m
    return -1


a = [0,1,2,3,4,5]

print(binary_search(a, 2))
print(binary_search(a, 6))
