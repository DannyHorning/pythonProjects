Apple_iPhone =	120.45
Android_Phone =	99.50
Apple_tablet =	75.69
Android_Tablet =	65.73
Windows_Tablet =	51.49
money_goals = 10000

n = 1
i = 1
f = 0

total_price = 0
price = 0

weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
business_weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

time_period = int(input("Enter:\n 1 - For specific Day \n 2 - For the Week \n 3 - For Week Business Days \n 4 - For Weekend days \n 0 - Exit" ))

while i<=1:
    if n == 2:
        n -= 1
    if time_period == 1:
        input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
    elif time_period == 2:
        n -= 1
        print(weekdays[f])
        f +=1
    elif time_period == 3:
        print (business_weekdays[f])
        f += 1
    elif time_period == 4:
        print (weekends[f])
        f += 1
    else:
        i += 1
    while n<=1:
        total_price += price
        price = 0
        phone_category = int(input("Enter product number 1-5, or enter 0 to stop: "))
        if phone_category != 0 and phone_category<= 5:
            product_sold = int(input("Enter quantity sold:  "))
            if phone_category == 1:
                price = Apple_iPhone * product_sold
            elif phone_category == 2:
                price = Android_Phone * product_sold
            elif phone_category == 3:
                price = Apple_tablet * product_sold
            elif phone_category == 4:
                price = Android_Tablet * product_sold
            elif phone_category == 5:
                price = Windows_Tablet * product_sold
        elif phone_category > 5:   
            print("Invalid input, please enter a valid number.")
        else:
            break
    print(total_price)

if total_price < money_goals:
    print("We didn't reach our goal for this period. More work is needed.")
else:
    print("You did well this period! Keep up the great work!”")
