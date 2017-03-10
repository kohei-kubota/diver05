def median(*args):
    arr = []
    for i in args:
        arr.append(i)
    k = 0
    w = 0
    i = len(arr) - 1
    index_med = round(i/2)
    while k < i:
        while True:
            if k <= i:
                if arr[i] < arr[i-1]:
                    w = arr[i-1]
                    arr[i-1] = arr[i]
                    arr[i] = w
                i = i - 1
            else:
                k = k + 1
                break
    return arr[index_med]

print(median(5,7,2))
print(median(7,3,2))
print(median(1,4,2))
