#Python Program to Find the Factorial of a Number
num= int(input('choose a number to find its factorials: '))

if num== 0:
    print('factorial number is one')
    if num >= 1:
        for i in range(1, num):
            result = i*i
            print(result)
    print('factorials for', num)
    if num < 1:
        print('factorial is not defined for this number')

