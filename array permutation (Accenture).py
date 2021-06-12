lst = list(map(int,input().split()))
sep = [] # List to separate out each integer
for i in lst: 
    for j in str(i):
        sep.append(int(j))
sep.sort() 
answer = ""
largest = sep[::-1] #sorting for the largest number to be first
for i in largest:
    answer += str(i)

print(answer)
