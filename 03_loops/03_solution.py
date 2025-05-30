number = 3

for i in range(1, 11):
    if i == 5:
        continue
    else:
        print(number, "X", i, " = ", number * i)