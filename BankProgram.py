def showbalance(balance):
    print(f"Your Balance is ${balance:.2f}")
def withdraw(balance):
    Amount=float(input("Enter any amount:  "))
    if Amount>balance:
        print("Insufficient funds")
    
    elif Amount<0:
        print("Invalid amount")
        
    else:
        return Amount

def deposit():
    Amount=float(input("Enter any amount:  "))
    if Amount<0:
        print("Invalid amount")
    else:
        return Amount
def main():
    running=True
    balance=0
    
    while running:
        print("**********************")
        print("   Banking program   ")
        print("**********************")
       # showbalance(balance)
        print("1.Show Balance",end="  ")
        print("2.Withdraw",)
        print("3.Deposit",end="       ")
        print("4.Exit")
        print("**********************")

        choice=input("Enter your choice(1-4):  ")

        if choice=="1":
         showbalance(balance)
        elif choice=="2":
            balance-=withdraw(balance) 
        elif choice=="3":
            balance+=deposit()
        elif choice=="4":
            running=False
        else :
            print("Invalid input")
    print("Thank You for coming")

main()


        
