def greatest_common_divisor(*args):
    arr = list(args)
    arr.sort()
    while True:
        arr = arr_for(arr)
        if len(arr) == 1:
            for i,data in enumerate(arr):
                if i == (len(arr) - 1):
                    break
                com_div.append(calcurate(data, arr[i+1]))
            break
    if arr[0] == 1:
        return "最大公約数が１です"
    return arr[0]

def arr_for(arr):
    com_div = []
    for i,data in enumerate(arr):
        if i == (len(arr) - 1):
            break
        com_div.append(calcurate(data, arr[i+1]))
    return com_div

def calcurate(x,y):
    while True:
        num = y % x
        if num == 0:
            return x
        else:
            y = x
            x = num


print(greatest_common_divisor(3,6,4,32,21,7,10))
print(greatest_common_divisor(30,20,10))
print(greatest_common_divisor(40,5,20,10))
print(greatest_common_divisor(13,11))
