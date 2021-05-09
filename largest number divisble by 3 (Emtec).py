numbers = list(map(int,input().split()))
divisble3 = []

for i in numbers:
    if i%3==0:
        divisble3.append(i)
    else:
        pass

print(max(divisble3))