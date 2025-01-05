import array as arr
arr = arr.array('i', [1, 7, 2, 89, 3])
def part(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    while start < end:
        while arr[start] <= pivot and start < ub:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[lb], arr[end] = arr[end], arr[lb]
    return end

print(part(arr))