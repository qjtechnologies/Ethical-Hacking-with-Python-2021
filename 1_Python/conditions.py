num1 = int(input("Enter a number: "))

if num1 > 10:
    print(f"Number {num1} is greater than 10")
elif num1 < 10:
    print("Number %d is less than 10" % (num1))
    print('Number {} is less than 10'.format(num1))
else:
    print("Number is 10")

# Number 22 is greater than 10

# print(num1)
