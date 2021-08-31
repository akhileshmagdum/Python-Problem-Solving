noOfCoins = int(input())
squared = []
if (noOfCoins<0):
    raise Exception("Enter the valid number of coins")
else:
    for i in range(1,noOfCoins+1):
        squared.append(i*i)
print(sum(squared))