num = int(input())
sumN = 0
for i in range (1,num):
    if (num%i==0):
        sumN = sumN + i
if (num == sumN):
    print(f"Perfect number: {num}")
else:
    print(f"Not an Perfect number: {num}")