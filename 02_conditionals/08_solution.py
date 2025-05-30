password = "himanshu123"
size = int(len(password))

if size < 6:
    pop_up = "Weak"
elif size > 10:
    pop_up = "Strong"
else:
    pop_up = "Medium"

print(pop_up)