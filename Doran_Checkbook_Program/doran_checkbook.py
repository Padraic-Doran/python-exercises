import locale
locale.setlocale( locale.LC_ALL, '' )




def current_balance():
    # Pulls current balance from .txt.
    
    f = open("balance.txt","r")
    contents = f.readlines()
    amt = 0.00
    for x in contents:
        x = float(x)
        amt = x + amt
    return amt
    



def withdraw(w):
    '''
    Withdraws amount of money, updates current balance
    '''
    w_money = abs((float(w)))
    f = open ("balance.txt", "a")
    f.write('\n')
    ledger = str((w_money) *-1)
    f.write(ledger)
    f = open("balance.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
        amtt = locale.currency(amt)
    print(
        '\n'
        'Current Balance: ' + amtt)
    f.close()
    

def deposit(m):
    '''
    Deposits amount of money entered into the function and
    displays updated current balance.
    '''
    deposit_m = abs((float(m)))
    f = open ("balance.txt", "a")
    f.write('\n')
    ledger = str(deposit_m)
    f.write(ledger)
    f = open("balance.txt","r")
    contents = f.readlines()
    amt = 0
    for x in contents:
        x = float(x)
        amt = x + amt
        amtt = locale.currency(amt)
    print(
        '\n'
        'Current Balance: ' + amtt)
    f.close()

# Accepts inputs 1-4.  Checks balance, allows withdrawals, 
# allows deposits.  If any other number is chosen it says invalid choice
# then returns to the main menu.

while True:
    print(
        "\n"
        "~~~ Welcome to your terminal checkbook! ~~~\n"
        "\n"
        "Your choices are below\n"
        "                           \n"
        "1) View Current Balance\n"
        "2) Make a Withdrawal\n"
        "3) Make a Deposit\n"
        "4) Exit\n"
    )
    choice = input("Please Enter a Choice: ")
    if choice == '1':
        balance = locale.currency(current_balance(), grouping=True)
        print('Current Balance: '+ balance)
    elif choice == '2':
        debit = input(f'Enter amount you would like to withdraw: $')
        withdraw(debit)
    elif choice == '3':
        credit = input(f'Enter amount you would like to deposit: $')
        deposit(credit)
    elif choice == '4':
        print(
            '\n'
            'Thanks! Have a nice Day. I hope you were whelmed.'
            '\n'
            )
        break
    else:
        print(
            '\n'
            'Invalid choice'
            '\n'
            )

