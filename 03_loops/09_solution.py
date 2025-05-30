list = ["apple", "banana", "orange", "apple"]

is_dplicate = False

for fruit in list:
    if list.count(fruit) > 1:
        is_dplicate = True
        print(fruit)
        break

if is_dplicate == False:
    print("There is no duplicates in the list")