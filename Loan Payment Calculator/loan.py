#Get loan details from user
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000
apr = float(input("What is the anual percentage rate? \n")) # 3%
payment = float(input("What will your monthly payments be, in dollars?\n")) # $1000
months = int(input("How many months do you want to see results for?\n")) # 24

#per month rate
monthly_rate = apr/100/12

for month in range(months):
    #Add in interest
    interest_paid = money_owed*monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("You paid off the load in", month+1, " months")
        break

    #Make Payment
    money_owed = money_owed - payment

    #Results after this month
    print("Paid", payment, "of which", interest_paid, " was interest", end=' ')
    print("Now I owe", money_owed)