input1 = int(input())
input2 = int(input())
n = int(input())
r = input2/input1
firstele = input1/r
print((firstele * (1- pow(r, n))) / (1 - r))