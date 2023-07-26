#Assignment 2: Profit Calculator
#Danny, Mahipinder, and Stadium. 

#Contant Variables
apple_iphone_price = 120.45
android_phone_price = 99.50
apple_tablet_price = 75.69
android_tablet_price = 65.73
windows_tablet_price = 51.49

apple_iphone_total = 0
android_phone_total = 0
apple_tablet_total = 0
android_tablet_total = 0
windows_tablet_total = 0

kill_switch = 1
catelog_stop = 1
days_stop = 0
weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

#Program Begin: includes program exit
print("Welcome to the Profit Calculator")
while kill_switch != 0:
    days_of_the_week = int(input("Enter how many days of the week you would like to calculate. \n1 - For a single day. \n2 - For a whole week. \n3 - For one work week (mon - fri). \n4 - For one weekend (sat - sun) \n0 - Exit "))
    kill_switch = days_of_the_week


    #loop for a single day
    if days_of_the_week == 1:
        specific_day = input("Which day of the week would you like to calculate? ")
        specific_day = specific_day.lower()
        specific_day = specific_day.capitalize()
        
        #convert string into th same format as the list. Loop until a word that exists in the list is entered
        while True:
            if specific_day not in weekdays:
                specific_day = input("Error: Please Enter the Day of the Week: ")
                specific_day = specific_day.lower()
                specific_day = specific_day.capitalize()
            else:
                break

        while days_stop < 1:
            while catelog_stop == 1:
                phone_category = int(input("Enter the phone category (as a number between 1-5) or 0 to exit: "))
                if phone_category == 0:
                    break
                elif phone_category <= 5 and phone_category > 0:
                    phone_quantity = int(input("Enter the quantity of phones sold: "))
                    if phone_category == 1:
                        apple_iphone_total = phone_quantity * apple_iphone_price
                    elif phone_category == 2:
                        android_phone_total = phone_quantity * android_phone_price
                    elif phone_category == 3:
                        apple_tablet_total = phone_quantity * apple_tablet_price
                    elif phone_category == 4:
                        android_tablet_total = phone_quantity * android_tablet_price
                    elif phone_category == 5:
                        windows_tablet_total = phone_quantity * windows_tablet_price
                else:
                    print("User Input Error. Please try again.", end=" ")
            days_stop += 1
        profit_daily = apple_iphone_total + android_phone_total + apple_tablet_total + android_tablet_total + windows_tablet_total
        print(f"Your daily profit total is: {profit_daily:.2f}")

        if profit_daily > 10000:
            print("Great work for today! Keep up the great work!")
        else:
            print("We didn't reach our goal today. More work is needed.")

    apple_iphone_total = 0
    android_phone_total = 0
    apple_tablet_total = 0
    android_tablet_total = 0
    windows_tablet_total = 0

    #loop for a whole week
    if days_of_the_week == 2:
        for days in weekdays:
            print("For",days)
            while catelog_stop == 1:
                phone_category = int(input("Enter the phone category (as a number between 1-5): "))
                if phone_category == 0:
                    break
                elif phone_category <= 5 and phone_category > 0:
                    phone_quantity = int(input("Enter the quantity of phones sold: "))
                    if phone_category == 1:
                        apple_iphone_total = phone_quantity * apple_iphone_price
                    elif phone_category == 2:
                        android_phone_total = phone_quantity * android_phone_price
                    elif phone_category == 3:
                        apple_tablet_total = phone_quantity * apple_tablet_price
                    elif phone_category == 4:
                        android_tablet_total = phone_quantity * android_tablet_price
                    elif phone_category == 5:
                        windows_tablet_total = phone_quantity * windows_tablet_price
                else:
                    print("User Input Error. Please try again.", end=" ")

            week_profit = apple_iphone_total + android_phone_total + apple_tablet_total + android_tablet_total + windows_tablet_total
        print(f"Your weekly profit total is: {week_profit:.2f}")

        if week_profit > 10000:
            print("Great work for this week! Keep up the great work!")
        else:
            print("We didn't reach our goal this week. More work is needed.")


        apple_iphone_total = 0
        android_phone_total = 0
        apple_tablet_total = 0
        android_tablet_total = 0
        windows_tablet_total = 0

    #loop for a work week (mon - fri)
    elif days_of_the_week == 3:
        for days in weekdays[0:5]:
            print("For",days)
            while catelog_stop == 1:
                phone_category = int(input("Enter the phone category (as a number between 1-5): "))
                if phone_category == 0:
                    break
                elif phone_category <= 5 and phone_category > 0:
                    phone_quantity = int(input("Enter the quantity of phones sold: "))
                    if phone_category == 1:
                        apple_iphone_total = phone_quantity * apple_iphone_price
                    elif phone_category == 2:
                        android_phone_total = phone_quantity * android_phone_price
                    elif phone_category == 3:
                        apple_tablet_total = phone_quantity * apple_tablet_price
                    elif phone_category == 4:
                        android_tablet_total = phone_quantity * android_tablet_price
                    elif phone_category == 5:
                        windows_tablet_total = phone_quantity * windows_tablet_price
                else:
                    print("User Input Error. Please try again.", end=" ")
            work_week_profit_3 = apple_iphone_total + android_phone_total + apple_tablet_total + android_tablet_total + windows_tablet_total
        print(f"Your work week profit total is: {work_week_profit_3:.2f}")
        if work_week_profit_3 > 10000:
            print("Great work for this period! Keep up the great work!")
        else:
            print("We didn't reach our goal this work week. More work is needed.")

        apple_iphone_total = 0
        android_phone_total = 0
        apple_tablet_total = 0
        android_tablet_total = 0
        windows_tablet_total = 0


    #Loop for the Weekend (sat -sun)
    elif days_of_the_week == 4:
        for days in weekdays[5: ]:
            print("For", days)
            while catelog_stop == 1:
                phone_category = int(input("Enter the phone category (as a number between 1-5): "))
                if phone_category == 0:
                    break
                elif phone_category <= 5 and phone_category > 0:
                    phone_quantity = int(input("Enter the quantity of phones sold: "))
                    if phone_category == 1:
                        apple_iphone_total = phone_quantity * apple_iphone_price
                    elif phone_category == 2:
                        android_phone_total = phone_quantity * android_phone_price
                    elif phone_category == 3:
                        apple_tablet_total = phone_quantity * apple_tablet_price
                    elif phone_category == 4:
                        android_tablet_total = phone_quantity * android_tablet_price
                    elif phone_category == 5:
                        windows_tablet_total = phone_quantity * windows_tablet_price
                else:
                    print("User Input Error. Please try again.", end=" ")
            weekend_profit = apple_iphone_total + android_phone_total + apple_tablet_total + android_tablet_total + windows_tablet_total
        print(f"Your weekend profit total is: {weekend_profit:.2f}")

        if weekend_profit > 10000:
            print("Great work for this weekend! Keep up the great work!")
        else:
            print("We didn't reach our goal this weekend. More work is needed.")

    elif days_of_the_week < 0 or days_of_the_week > 4:
        print("User Input Error. Please try again.", end=" ")
    
    elif days_of_the_week == 0:
        print("Program End!")

    else:
        continue