parts = list(map(int,input().split())) #getting parts input

parts.sort()
answer = [] #list for appending the addition combination

for i in range(len(parts)-1):
    add = parts[i] + parts[i+1] # adding to adjecent elements
    parts[i+1] = add #converting the addition
    answer.append(add)

print(sum(answer))