string = list(input().split())
answer = ""
for i in string:
    answer += i[::-1]
    answer +=" "
print(answer)