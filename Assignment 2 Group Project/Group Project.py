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

catelog_stop = 1

while catelog_stop == 1:
    phone_category = int(input("Enter the phone category (as a number between 1-5): "))
    if phone_category == 0:
        break
    phone_quantity = float(input("Enter the quantity of phones sold: "))
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

profit_daily = apple_iphone_total + android_phone_total + apple_tablet_total + android_tablet_total + windows_tablet_total

print(f"Your daily profit total is: {profit_daily:.2f}")