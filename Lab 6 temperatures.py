temp_list = []
temperature = float(input("Enter a temperature: "))
while temperature < 999:
    temp_list.append(temperature)
    temperature = float(input("Enter another temperature: "))

total_temp = 0
temp_count = 0
above_average_count = 0

for temps in temp_list:
    total_temp += temps
    temp_count += 1
temp_average = total_temp / temp_count

for temps in temp_list:
    if temp_average < temps:
        above_average_count += 1
    else:
        continue
print(f'{above_average_count} temperatures were above the average of {temp_average:.1f}')
