def nearest(arr, i):
    for j in range(1, len(arr)):
        low = i - j
        high = i + j
        if 0 <= low and arr[low] > arr[i]:
            return low
        if high < len(arr) and arr[high] > arr[i]:
            return high

x = [1, 5, 3, 2, 6, 7, 14, 0, 4]
print(nearest(x, 3))