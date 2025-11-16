import os

count = int(input("How many bank accounts do you want to create? "))

names = []     
balances = []   

i = 0
while i < count:
    name = input(f"Account holder name {i+1}: ")
    balance = float(input(f"Initial balance for {name}: "))
    names.append(name)
    balances.append(balance)
    i += 1
    
    os.system('cls')


while True:
    

    
    print("1. Show all account balances")
    print("2. Deposit to an account")
    print("3. Withdraw from an account")
    print("4. Show accounts above average balance")
    print("5. Exit")

    choice = input("Choose an option: ")


    if choice == "1":
        print("\nAccounts list:")
        i = 0
        while i < count:
            print(f"\033[92m{names[i]}\033[0m --> Balance: \033[92m{balances[i]}\033[0m ")
            i += 1


    elif choice == "2":
        name = input("Enter the account name: ")
        if name in names:
            index = names.index(name)
            amount = float(input("Deposit amount: "))
            balances[index] += amount
            print("\033[92mDeposit successful.\033[0m")
        else:
            print("\033[91mAccount not found!\033[0m")


    elif choice == "3":
        name = input("Enter the account name: ")
        if name in names:
            index = names.index(name)
            amount = float(input("Withdrawal amount: "))
            if balances[index] >= amount:
                balances[index] -= amount
                print("\033[92mWithdrawal successful.\033[0m")
            else:
                print("\033[91mInsufficient balance!\033[0m")
        else:
            print("\033[91mAccount not found!\033[0m")


    elif choice == "4":
        total = 0
        i = 0
        while i < count:
            total += balances[i]
            i += 1

        avg = total / count

        print(f"\nAverage balance: {avg}")
        print("Accounts with balance above average:")

        i = 0
        found = False
        while i < count:
            if balances[i] > avg:
                print(f"\033[92m{names[i]}\033[0m --> Balance: \033[92m{balances[i]}\033[0m")
                found = True
            i += 1

        if not found:
            print("No account is above the average.")


    elif choice == "5":
        break

    else:
        print("\033[91mInvalid option!\033[0m")
