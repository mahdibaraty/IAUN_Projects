Num = input("Please enter a Tow-digit Number: ")

if len(Num) == 2:
    Tens = int(Num) // 10
    Units = int(Num) % 10
    ReversedNum = f"{Units}{Tens}"
    print(f"Reversed Number is :{ReversedNum}")
else:
    print("Number is not True")