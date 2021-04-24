alphabet = [' ','A' ,'B' ,'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] #alphabet list with space as [0]
code = list(input().split()) #Input

for i in range(len(code)):
    if code[i]=="_":
        code.remove('_')
        code.insert(i,0)
    elif code [i]=='#':
        hashlist = code[i-1:] #list for symbols
        numlist = code[:i-1] #list for numberarray

intoint = [] #list to convert str into int
conversion = [] #list are required for conversion

for i in numlist:
    intoint.append(int(i)) #str to int conversion

for i in intoint:
    conversion.append(alphabet[i]) #decoding numbers into alphabets

for j in range(len(hashlist)): #decoding of symbols
    if hashlist[j] == '#':
        hashlist[j] = ' '

ans = "" #final answer in str format

conversion.extend(hashlist) #combining both

for i in conversion: #list to str conversion
    ans += i

print(ans)