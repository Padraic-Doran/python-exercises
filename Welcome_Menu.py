def menu():
    # money = int(self.balance)
    # money = float(money)
    #printing options available
    print("Welcome")
    current_customer = input("Are you a current customer? Y/N: ")
    if current_customer.lower() == "y":
        print("What would you like to do today?")
        print("---------------------------------")
        print("1) Check Balance")
        print("2) Withdraw Money")
        print("3) Deposit Money")
        print("4) Quit")
        return input("Choose your option: ")
    if current_customer.lower() == "n":
        return ("Bruh, you gotta sign up at a local branch before you can access this app. Goodbye!")
        # return sys.exit()
    else:
        print("Invalid choice, please try again")
        return menu()


print(menu())