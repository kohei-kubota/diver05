def compare_age(num1=40,num2=20):
    if isinstance(num1, str) or isinstance(num2, str):
        try:
            num1 = int(num1)
            num2 = int(num2)
        except ValueError:
            return
    if num1 > 30:
        print('◯◯')
        if num2 < 30:
            print('☓☓')

compare_age()
compare_age(29, 29)
compare_age("40", "40")
compare_age("this", "that")
