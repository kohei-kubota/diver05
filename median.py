def median(*args):
    arr = list(args)
    k = 0
    w = 0
    i = len(arr) - 1
    index_med = round(i/2)
    while k < len(arr) - 1:
        while k < i:
            if arr[i] < arr[i-1]:
                w = arr[i-1]
                arr[i-1] = arr[i]
                arr[i] = w
                i = i - 1
                if k >= i:
                    k = k + 1
                    i = len(arr) - 1
            else:
                i = i - 1
                if k >= i:
                    k = k + 1
                    i = len(arr) - 1
    return arr[index_med]

print(median(5,7,2))
print(median(7,3,2))
print(median(1,4,2))
print(median(4,2,1))
print(median(1,2,4))
print(median(3,6,4,32,21,7,10))
