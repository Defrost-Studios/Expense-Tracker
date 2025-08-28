#Personal Expense Tracker


import csv
from datetime import datetime
#FUNCTIONS

def add_transaction(cost, catagory, description): # function that basically adds the transcation into the csv file
    date = datetime.now().strftime("%Y-%m-%d") # variable with the actual date
    with open("Personal Expense Tracker/expenses.csv", mode="a", newline="") as file: # opens(creates) a csv file titled expenses and appends(mode ="a") on a new line
        writer = csv.writer(file) # creates a csv "writer object" that puts data into the file
        writer.writerow([date, cost, catagory, description]) # writes down the data on a new file

def view_transactions():
    try:
        with open("Personal Expense Tracker/expenses.csv", mode="r") as file: #function that lets you view your expenses
            reader = csv.reader(file) #creates variable called reader and links it to csv.reader
            print("\n ----[Expenses]----")#title
            for row in reader: #sets up the list
                date, cost, catagory, description = row #headings or lables for columns
                print(f"{date} | ${cost} | {catagory} | {description}") #prints the information from the csv file
    except FileNotFoundError: #if there is no file, it will say that there are no expenses yet
        print("No expenses added yet")

#MAIN
 
print("WELCOME TO YOUR EXPENSE TRACKER \n")

q = False
while q == False:
    choice = int(input("what do you want to do? \n (1)add expense \n (2)view expenses \n (3)Exit \n"))
    if choice == 1:
        Money = (input("enter your item cost: "))
        cata = (input("enter catagory of item: "))
        desc = (input("enter item desc: "))
        add_transaction(Money, cata, desc)
        print("---[Expense Added!]---")
    elif choice == 2:
        view_transactions()
    elif choice == 3:
        q = True
    else:
        print("invalid response")

