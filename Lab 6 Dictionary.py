nwt_pop = int(input("Enter the population for the North West Territories: "))
yukon_pop = int(input("Enter the population for the Yukon: "))
nunavut_pop = int(input("Enter the population for Nunavut: "))

pop_total = nwt_pop + yukon_pop + nunavut_pop

pop_dictionary = {'North West Territories':nwt_pop, 'Yukon':yukon_pop, 'Nunavut':nunavut_pop, 'Total Population': pop_total}

for place, pop in pop_dictionary.items():
    print(place, pop)