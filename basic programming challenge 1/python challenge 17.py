def listOfOddNumbers(a,b):
    if a % 2 == 0:
        a = a + 1
    odds = list(range(a,b,2))
    return odds
print(listOfOddNumbers(1,100))
