def greatest_common_divisor(*args):
    arr = list(args)
    while True:
        arr = arr_for(arr)
        if len(arr) == 1:
            break
    if arr[0] == 1:
        return "公約数はありません"
    return arr[0]

def arr_for(arr):
    com_div = []
    for i,data in enumerate(arr):
        if i == (len(arr) - 1):
            break
        com_div.append(calcurate(data, arr[i+1]))
    return com_div

def calcurate(x,y):
    if x > y:
        while True:
            num = x % y
            if num == 0:
                return y
            else:
                x = y
                y = num
    else:
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
