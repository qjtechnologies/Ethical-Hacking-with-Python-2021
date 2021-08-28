# def addition(num1, num2):
#     a = num1
#     b = num2
#     c = a+b
#     return c


# x = addition(25, 35)
# print("Value of x", x)
# y = addition(22, 32)
# print(x, y)


x = 100


def tester():
    # global x
    x = 105
    print(x)


print(x)
tester()
print(x)
