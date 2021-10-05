a = int(input())
lst = list(map(int,input().split()))

sumed = []
lstSum = []

for i in lst:
    for j in lst:
        product = i * j

        tempLst = []
        tempLst.append(i)
        tempLst.append(j)

        lstSum.append(tempLst)
        sumed.append(product)

minInSumed = min(sumed)

answer = sumed.index(minInSumed)

print(answer)