parts = list(map(int,input().split())) #getting parts input
parts.sort()
answer = []
print(len(parts))
for i in range(len(parts)-1):
    add = parts[i] + parts[i+1]
    parts.remove(parts[i])
    parts.remove(parts[i])
    parts.insert(0,0)
    parts.insert(1,0)
    answer.append(add)

print(answer)