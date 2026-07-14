user_account = {
    "pin" : 2468,
    "balance" : 20000,
    "name" : "kamal sri raj"
}
attempts = 3
while attempts > 0:
    password = int(input("Enter the 4-digit pin: "))
    if password == user_account["pin"]:
        print(f"pin verified. Welcome {user_account['name']}")
        break
    elif password != user_account["pin"]:
        attempts = attempts - 1
        print(f"Incorrect pin. You have {attempts} attempts")
if attempts == 0:
    print("Your account is locked. Please visit your your local branch")
else:
    amount = float(input("Enter the amount you want to withdraw:"))
    if amount > user_account["balance"]:
        print("Transaction denied: Insufficient balance")
    elif amount < user_account["balance"]:
        print(f"Transaction successful! You withdraw {amount}")
        current_balance = user_account["balance"] - amount
        print(f"Your's current balance is {current_balance}")

