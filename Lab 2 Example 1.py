current_price = int(input("Enter Current Price:"))
last_month_price = int(input("Enter Last Month Price:"))
change_price = current_price - last_month_price
monthly_mortgage = (current_price*0.051) / 12
print("Current Price Is:" , current_price)
print("Change of Price:" , change_price)
print("Monthly Mortgage" , monthly_mortgage)
