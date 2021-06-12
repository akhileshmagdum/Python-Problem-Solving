lst = list(map(int,input().split()))
sep = []
for i in lst:
    for j in str(i):
        sep.append(int(j))
sep.sort()
answer = ""
largest = sep[::-1]
for i in largest:
    answer += str(i)

print(answer)
