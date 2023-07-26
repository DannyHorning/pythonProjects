#Welcome Message
print("Welcome to the Global Energy bill calculator!")
#Have customer input their account number
account = int(input("Enter Your Account Number"))

#Have customer input the number of month
month = int(input("Enter the month number (e.g., for January, enter 1)"))

#Select Electricity Plan
electricity_plan = input("Enter your electricity plan (EFIR or EFLR)")

#input the amount of electricty used
electricity_useage = int(input("Enter Your Electricity Useage (in kWh): "))

#The Electricity prices
EFIR_low = 0.0836
EFIR_high = 0.0941
EFLR_rate = 0.0911
monthly_electric_fee = 120.62

#Calculate electricity price
if electricity_plan == "EFIR":
    if electricity_useage <= 1000:
        electricity_price = EFIR_low * electricity_useage
    else:
        electricity_price = (EFIR_low * 1000) + (EFIR_high * (electricity_useage - 1000))
else:
    electricity_price = EFLR_rate * electricity_useage

#Add monthly electric fee
electric_gross = electricity_price + monthly_electric_fee

#input Gas Plan
gas_plan = input("Please Enter Your Selected Gas Plan: ")

#input the amount of gas used
gas_useage = int(input("Please Enter the Amount of Gas Used (in GJ): "))

#The Gas Prices
GFIR_low = 0.0456
GFIR_high = 0.0589
gflr = 0.0393
monthly_gas_fee = 1.32

#Calculate the gas price
if gas_plan == "GFIR":
    if gas_useage <= 950:
        gas_price = gas_useage * GFIR_low
    else:
        gas_price = (GFIR_low * 1000) + (gflr * (gas_useage - 1000))
else:
    gas_price = gflr * gas_useage

#Add monthly Gas Fee
gas_gross = gas_price + monthly_gas_fee

#input province
province = input("Please Input Your Province (abbreviated): ")

#Provincial Tax Rates
ON_tax = 1.13
maritime_tax = 1.15
canada_tax = 1.05

#Add provincial Tax:
if province == "ON":
    price_final = (gas_gross + electric_gross) * ON_tax
elif province == "NB" or province == "NL" or province == "NS" or province == "PEI":
    price_final = (gas_gross +electric_gross) * maritime_tax
else:
    price_final = (gas_gross+electric_gross) * canada_tax

#print the final price
print(f"Thank you! Your total amount due now is: {price_final:.2f}")