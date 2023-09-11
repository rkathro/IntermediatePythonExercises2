from BankAccount import BankAccount

def main():
    #Create BankAccount object with name and starting balance
    sample_account = BankAccount("Wally", 500)

    #Deposit 500
    sample_account.deposit(500)

    #Withdraw 929.84
    sample_account.withdraw(929.84)

    #Print balance
    print(sample_account.get_balance())

main()