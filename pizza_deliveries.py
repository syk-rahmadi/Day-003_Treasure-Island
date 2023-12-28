print("Thank you for choosing Python Pizza Deliveries.")
size = input("Please choose your size (S,M,L)!")
pepperoni_toping = input("Do you want add pepperoni toping (Y,N)?")
extra_cheese = input("Do you want add extra cheese (Y,N)?")

# small = 20
# medium = 30
# large = 40

# small_topping = 2
# medium topping = 3
# larger_topping = 4

# extra_cheese_small = 1
# extra_cheese_medium = 2
# extra_cheese_large = 3


total_bill = 0

if size == "S":
    total_bill += 20
elif size == "M":
    total_bill += 30
else:
    total_bill += 40

if pepperoni_toping == "Y":
    if size == "S":
        total_bill += 2
    elif size == "M":
        total_bill += 3
    elif size == "L":
        total_bill += 4

if extra_cheese == "Y":
    if size == "S":
        total_bill += 1
    elif size == "M":
        total_bill += 2
    elif size == "L":
        total_bill += 3

print(f"Your final bill is: {total_bill}")
