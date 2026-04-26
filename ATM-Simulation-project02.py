import datetime

print("Welcome to the ATM Simulation")
password = 114
balance = 2000
Transcations = []
attempt = 0
max_attempts = 4

while attempt < max_attempts:
    pin = int(input("Please enter your 4 digit PIN: "))

    if pin == password:
        print("\n You have successfully logged in:")

        while True:
            print("\n --- Select an option ---")
            print("1. Check balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Record Statement")
            print("5. Exit")

            choice = int(input("Please Enter Number (1/2/3/4/5): "))

            if choice == 1:
                print(f"Current balance : Rs {balance}")

            elif choice == 2:
                deposit_money = int(input("Please enter your deposit amount: "))
                balance += deposit_money
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Transcations.append((time , f"deposit_money: Rs {deposit_money}"))
                print(f"deposit successfull ! New balance : {balance}")

            elif choice == 3:
                withdraw_money = int(input("Please enter your withdraw amount: "))
                if withdraw_money <= balance:
                    balance -= withdraw_money
                    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    Transcations.append((time, f"Withdraw | Rs {withdraw_money}"))
                    print(f"withdraw successful ! Remaining balance : {balance}")
                else :
                    print("Insufficient funds")


            elif choice == 4:
                print("\n--- Record Statement ---")
                if not Transcations:
                    print("No transactions made")
                else:
                    for t in Transcations:
                        print(f"{t[0]} -> {t[1]}")
                print(f"Available Balance : Rs {balance}")

            elif choice == 5:
                print("\n ---Exit---")
                print('Thank you for using this ATM simulation Machine ! Please visit Again !')
                break
            else:
                print("Invali input please select one of the option ")
                break


    else:
        attempt += 1
        remaining = max_attempts - attempt
        print(f" Incorrect pin ! Attempts left : {remaining}")
        if remaining == 0:
            print("Account blocked! Please try again after some time:")
            break








