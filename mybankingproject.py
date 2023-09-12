customername=["revanth","raghu","hafeez","lokesh","ameen"]
customerpin=[1111,2222,3333,4444,5555]
customerbalance=[1000,2000,3000,4000,5000]
deposit=0
withdraw=0
balance=0
counter_1=1
counter_2=5
i=0 #Tempory variable

while True: #for infinite loop
    print("WELCOME TO MY BANK")
    print("1.Account open")
    print("2.Withdraw Money")
    print("3.Deposite Money")
    print("4.Check Customers and Balance")
    print("5.Exit")
    option=input("enter your chioce: ")
    if option=="1":
        print("customer is has selected option 1")
        numberofcustomers=eval(input("Number of customers: ")) #eval means 1+3=4 or 1,2,3,4=10
        i=i+numberofcustomers
        if i>5:
            print("\n")
            print("customer registration exceed reached or customer registration too low")
            i=i-numberofcustomers
        else:
            while counter_1<=i:
                name=input("Enter Customer Name: ")
                customername.append(name)
                pin=str(input("Create Your Own Pin: "))
                customerpin.append(pin)
                blance=0
                deposite=eval(input("please input a pin of your chioce: "))
                balance= balance+deposit
                customerbalance.append(balance)
                print("\nName=",end=" ")
                print(customername[counter_2])
                print("Pin",end=" ")
                print(customerpin[counter_2])
                print("balance=",end=" ")
                print(customerbalance[counter_2],end=" ")
                print("Rs/-")
                counter_1=counter_1+1
                counter_2=counter_2+1
                print("\nYour name is added to the Bank account")
                print("Your pin is added to our bank system")
                print("Your account created")
                print("\n")
                print("your name is added available on the customer list now:")
                print(customername)
                print("\n")
                print("please remember your name and pin")
            mainmenu=input("to goto main menu press any key ")
    elif option=="2":
        j=0
        print("Chioce number 2 is selected by the customer")
        while j<1:
            k=-1
            name=input("Enter your Name: ")
            pin=input("Enter your Pin: ")
            while k<len(customername)-1:
                k=k+1
                if name==customername[k]:
                    if pin==customerpin[k]:
                        j=j+1
                        print("Your current Balance:",end="")
                        print(customerbalance[k],end=" ")
                        print("rs/-\n")
                        balance=(customerbalance[k])
                        withdraw=eval(input("input value withdraw: "))
                        if withdraw>balance:
                            deposit=eval(input("Please add high amount: "))
                            balance=balance+deposit
                            print("your current balanceis:",end=" ")
                            print(balance,end=" ")
                            print("rs/-\n")
                            balance=balance-withdraw
                            print("\n")
                            print("withdraw successfull")
                            customerbalance[k]=balance
                            print("Your new balance: ",balance,end=" ")
                            print("rs/-\n\n")
                        else:
                            balance=balance-withdraw
                            print("\n")
                            print("withdraw Successfull")
                            customerbalance[k]=balance
                            print("your new balance: ",balance,end=" ")
                            print("rs/-\n\,n")
                    if j<1:
                        print("your name and pin does not match\n")
                        break
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ")
    elif option=="3":
        print("Customer has selected 3rd option")
        n=0
        while n<1:
            k=-1
            name=input("Name: ")
            pin=int(input("password: "))
            while k<len(customername)-1:
                k=k+1
                if name==customername[k]:
                    if pin==customerpin[k]:
                        n=n+1
                        print("your Current Balance: ",end=" ")
                        print(customerbalance[k],end=" ")
                        print("Rs/-")
                        balance=(customerbalance[k])
                        deposit=eval(input("Please Enter how much you want to deposite: "))
                        balance=balance+deposit
                        customerbalance[k]=balance
                        print("\n")
                        print("Deposite successful")
                        print("Your New Balance: ",balance,end=" ")
                        print("Rs/-\n\n")
            if n<1:
                print("Your name and pin does not match \n")
                break
        mainmenu=input("Please press enter key to go back to main menu to perform another function or exit ")
    elif option=="4":
        print("chioce number 4 is selected by the customer")
        k=0
        print("customer name list and balance mention below: ")
        print("\n")
        while k<=len(customername)-1:
            print("Customer =",customername[k])
            print("Balance =",customerbalance[k],end=" ")
            print("rs/-")
            print("\n")
            k=k+1
        mainmenu=input("please press enter key to go back to main menu to perform another fuction or exit ")
    elif option=="5":
        print("chioce number 5 selected by customer")
        print("Thank you for using for MY banking system")
        print("\n")
        print("Come again")
        print("Namasta")
        break
    else:
        print("Invalid Option Selected by the Customer")
        print("please try again")
        mainmenu=input("please press enter key to go back to main menu to perform another function or exit ")


        







                


