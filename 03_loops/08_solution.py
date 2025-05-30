number = 46
flage = True
if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print("NOT a prime number")
            flage = False
            break
    
if flage:
    print(number, "is a prime number")