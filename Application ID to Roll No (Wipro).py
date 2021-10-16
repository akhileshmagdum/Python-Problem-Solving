appid = input()
sum = 0
adjust = 0
alpha = ['_','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for num in appid:
    sum += int(num)
if sum >26:
    x = str(sum)
    for i in x:
        adjust += int(i)
    print(alpha[adjust])
else:
    print(alpha[sum])