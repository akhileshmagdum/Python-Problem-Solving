def sumofmultiplications(arr1,arr2,size):
    lst = [] #list to store multiplications
    rev = arr2[::-1] #rversing the second array
    
    for i in range(len(arr1)):
        lst.append(arr1[i]*rev[i])

    return (sum(lst))

array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
size = 68

print(sumofmultiplications(array1,array2,size))