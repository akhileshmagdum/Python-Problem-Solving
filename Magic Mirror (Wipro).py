alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

num = int(input())
x = [int(a) for a in str(num)]

ans =[]

for i in x:
    ans.append(alpha[i])

print(*ans,sep="")