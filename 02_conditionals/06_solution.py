distance = 10

if distance < 3:
    suggest = "Walk"
elif distance >= 3 and distance <= 15:
    suggest = "Bike"
elif distance > 15:
    suggest = "Car"

print(suggest)