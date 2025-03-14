import array as arr
arr = arr.array('i', [1, 7, 2, 89, 3])
def part(arr, lb, ub):
    pivot = arr[lb]
    start = lb
    end = ub
    
    while True:
        while start < end and arr[start] <= pivot:
            start += 1
        while start < end and arr[end] >= pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
        else:
            break