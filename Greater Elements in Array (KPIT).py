inArr = list(map(int,input().split()))
inArrSum = sum(inArr)
average = inArrSum/len(inArr)
greaterArr = []
for i in inArr:
    if i>=average:
        greaterArr.append(i)
print(len(greaterArr))