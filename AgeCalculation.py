Age = int(input("Please enter your age in years: "))

days = Age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your age in Hours \033[92m{hours}\033[0m, Minutes \033[92m{minutes}\033[0m and Seconds \033[92m{seconds}\033[0m")
