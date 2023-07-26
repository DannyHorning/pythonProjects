weekdays = ["monday", 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
days_stop = 0

print("Welcome to the Profit Calculator")

days_of_the_week = int(input("Enter how many days of the week you would like to calculate. 1 for one day. 2 for a whole week. 3 for one work week (mon - fri). 4 for one weekend (sat - sun) "))