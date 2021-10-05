n = int(input())
k = int(input())

lst = []
newList = []

for i in range(n):
    e = int(input())
    lst.append(e)

for j in lst:
    q =j//k
    newList.append(q)

print(sum(newList))