numberTodecode= int(input('Enter your number:'))
def factorFinder(numberTodecode):
    trynum= 0
    endList= []
    while trynum <= (numberTodecode/2):
        trynum += 1
        if numberTodecode % trynum == 0:
            num2= numberTodecode//trynum
            endList.append(trynum)
            endList.append(num2)
        else:
            continue
    return(endList)
def duplicateRemover(list):
    bigboy=int(((len(list))/2))
    for a in range (1, bigboy):
        list.remove(list[a])
    return list
def primeFactorfinder()
factors=factorFinder(numberTodecode)
factors.sort()
factors= duplicateRemover(factors)
print('Factors of', numberTodecode, 'are', factors)
primefactors= []
for y in range (0, len(factors)):
    factorp= factors[y]
    while factorp % 2 ==0:
        factorp= factorFinder(factorp)
    primefactors.append(factorp)
    continue
primefactors.sort()
primefactors= duplicateRemover(primefactors)
print('Prime factors of', numberTodecode, "are", primefactors)