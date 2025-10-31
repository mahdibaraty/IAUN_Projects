Num = input("Please enter a Tow-digit Number: ")

if len(Num) == 2:
    Tens = int(Num) // 10
    Units = int(Num) % 10
    A = Tens
    B = Units
    Expt1 = Tens ** Units
    Expt2 = Units ** Tens
    print(f"First Number is: \033[92m{A}\033[0m Second Number is: \033[92m{B}\033[0m")
    print(f"{Tens}^{Units} = {Expt1}")
    print(f"{Units}^{Tens} = {Expt2}")
else:
    print("Number is not True")