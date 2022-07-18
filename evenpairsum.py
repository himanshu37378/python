a = int(input("enetr the first integer"))
b = int(input("enetr the second integer"))
value = 0
for x in range(a):
    for y in range(b):
        sum = x + y
        if (sum % 2 == 0):
            value = value + 1
print(count)