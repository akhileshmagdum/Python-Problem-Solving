def findmax(lit): #function returns the largest number
    lit.sort()
    return lit[-1]

def find2max(lit): #function returns the second largest number
    lit.sort()
    return lit[-2]

num = input()
lst = list(num.split(" ")) #separating each number
bigboy = [] #list with nested list containing separate digits
addition = [] #list with result of substraction from each list
kashi = 0 #total addition of substracted values

for each in lst:
    seplist = [] #splitted list of each digit of every integer
    for eachagain in str(each):
        integer = int(eachagain) #converting from str to int
        seplist.append(integer)
    bigboy.append(seplist)

for i in range(0,(len(bigboy))): # to iterate through each sublist of the nested list
    maxx = findmax(bigboy[i])
    maxx1 = find2max(bigboy[i])
    addition.append(maxx-maxx1) #list will all the substracted values
    
for i in addition: #addition of the values
    kashi +=i
print(kashi)