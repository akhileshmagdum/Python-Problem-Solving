inp = int(input())
num = [int(a) for a in str(inp)]

aseceding = sorted(num)

reversedList = []
for i in aseceding:
    reversedList.append(i)
    
reversedList.sort(reverse=True)

ascListForConversion = [str(i) for i in aseceding]
asc = "".join(ascListForConversion)
intAsc = int(asc)

decListForConversion = [str(i) for i in reversedList]
des = "".join(decListForConversion)
intDesc = int(des)

addition = intAsc+intDesc

print(addition)