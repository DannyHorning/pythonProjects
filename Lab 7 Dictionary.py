thisDict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
thatDict = {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}


def lengthOfValues(dictionary):
    valuesList = dictionary.values()
    newDict = {}
    for i in valuesList:
        newDict[i] = len(i)
    return newDict


print(lengthOfValues(thisDict))
print(lengthOfValues(thatDict))