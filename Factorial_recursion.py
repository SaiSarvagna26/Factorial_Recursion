def factorial(number):
    if number<=1:
        return 1
    else:
        return factorial(number-1)*number

number=int(input())
print(factorial(number))