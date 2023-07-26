def countEvens(tupleOfNumbers):
    numberOfEvens = 0
    for numbers in tupleOfNumbers:
        if numbers % 2 == 0:
            numberOfEvens += 1
    print(numberOfEvens)

def countOdds(tupleOfNumbers):
    numberOfOdds = 0
    for numbers in tupleOfNumbers:
        if numbers % 2 != 0:
            numberOfOdds += 1
    print(numberOfOdds)

tupleOfNumbers = (1,2,3,4,5,6,7,8,9)

countEvens(tupleOfNumbers)
countOdds(tupleOfNumbers)
