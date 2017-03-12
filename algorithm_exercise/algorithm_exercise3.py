def sort(*args):
    arr = list(args)
    arr = []
    for j in args:
        for l in j:
            if isinstance(l,int):
                l = str(l)
            arr.append(l)

    k = 0
    w = 0
    i = len(arr) - 1
    index_med = round(i/2)
    while k < len(arr) - 1:
        while k < i:
            if arr[i-1] < arr[i]:
                w = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = w
                i = i - 1
                if k >= i:
                    k = k + 1
                    i = len(arr) - 1
            else:
                i = i - 1
                if k >= i:
                    k = k + 1
                    i = len(arr) - 1
    return arr

sample_list = ['a', 'b', 'c']
print(sort(sample_list))
sample_list = [1, 2, 3]
print(sort(sample_list))
sample_list = [1, 2, 3,'a', 'b', 'c']
print(sort(sample_list))
