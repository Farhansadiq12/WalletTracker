# Code for Wallet Tracker.


import datetime
import calendar
from datetime import date
from calendar import monthrange


def number_of_days_in_month(year=date.today().year,month=date.today().month):
    return monthrange(year,month)[1]

#Inputting Transactions for the month

expenditure_array={ "1" : 200, "2" : 150, "3" : 80, "4" : 90, "5" : 55, "6" : 89, "7" : 120, "8" : 98, "9" : 99, "10" : 99, "11" : 89, "12" : 27, "13" : 89, "14" : 20,                 "15" : 98, "16" : 123, "17" : 90, "18" : 101, "19" : 110, "20" : 150, "21" : 111,
                    "22" : 165, "23" : 81, "24" : 109,"25" : 99,"26" : 98,"27" : 110, "28" : 29, "29" : 89, "30" : 176, "31" : 230,}

today = date.today()
d = today.strftime("%d")
now = datetime.datetime.now()

d_total = 0

#Take input for income
print("Enter your income: ")
TrueIncome = int(input())
print("Income: "+str(TrueIncome))

string = " "
Recurring = [ ]
recurTotalCost=0

#Take input for recurring payments
while string.upper() != "NO":
    print("Type of recurring payment: ")
    recur = input()
    print("Cost of recurring payment: ")
    recurCost = int(input())
    elements = [recur,recurCost]
    Recurring.append(elements)
    string = (input("Do you have more recurring payments?(Yes/No) "))
    recurTotalCost = recurCost + recurTotalCost

    
   
print(Recurring)
print("\n")
print("Total Recurring Cost: $"+str(recurTotalCost))
print("\n")

#Asking for saving goals
print("What Percentage of your income do you want to save this month?")
saved_percentile = input()
Goal = TrueIncome * (int(saved_percentile) / 100)
print("So this month, you want to save $",Goal)

CurrentSavings =TrueIncome - recurTotalCost

if (CurrentSavings<recurTotalCost):
    print("Your Cost has exceeded your income!")
else:
    print("You are on track to save money!")

print("\nLiquid Money Expense Amount: $"+str(CurrentSavings))

DailyLimit = CurrentSavings * (1 / number_of_days_in_month(date.today().year,date.today().month))
print("\nYour limit for today is: $"+"%.2f" % DailyLimit)
if(DailyLimit < 0):
    print("ALERT: You are overspending!!!")

#Evaluation of your daily expense
print("Today's expenditure: $",expenditure_array[d])


saved_amount = DailyLimit - int(expenditure_array[d])
exceeded_amount = int(expenditure_array[d]) - DailyLimit
d_save=Goal-saved_amount

if(expenditure_array[d] > DailyLimit ):
    print("You have exceeded the limit! The amount you have exceeded is $",exceeded_amount)
    print("You are $"+"%.2f" % d_save,"far from your goal")
elif(expenditure_array[d] == DailyLimit):
    print("You are on the limit. You have saved $0")
else:
    print("YAY! Today you saved $"+"%.2f" % saved_amount)  
    print("You are $"+"%.2f" % d_save,"closer to your goal")


#To see your previous transactions.
string = " "
while string.upper() != "NO":
    print("Do you want to see your previous transaction?(Yes/No)")
    string = input()
    if string.upper()!="NO":
        print("Which day's spending summary do you want to see?")
        d = input()
        print("Expenditure for the",d + "th is $", expenditure_array[d])
        saved_amount = DailyLimit - int(expenditure_array[d])
        exceeded_amount = int(expenditure_array[d]) - DailyLimit
        if(expenditure_array[d] > DailyLimit ):
            print("You have exceeded the limit! The amount you have  exceeded is $",exceeded_amount)
        elif(expenditure_array[d] == DailyLimit):
            print("You are on the limit. You have saved $0")
        else:
            print("YAY! That day you saved $"+"%.2f" % saved_amount) 
    
