def momDad(S,namelist):

    lst = []

    for s in namelist:
        lenOfInput = len(S)
        lenOfWord = len(s)
        store_res = [[0]*(lenOfWord+1)for i in range (lenOfInput+1)]
        
        for i in range(lenOfWord+1):
            store_res[0][i] = 0

        for i in range(lenOfInput+1):
            store_res[i][0] = 1

        for i in range(1,lenOfInput+1):

            for j in range(1,lenOfWord+1):

                if S[i-1]==s[j-1]:
                    store_res[i][j]= store_res[i-1][j-1]+store_res[i-1][j]
                else:
                    store_res[i][j] = store_res[i-1][j]


        res = store_res[lenOfInput][lenOfWord]
        lst.append(res)

        
    print(sum(lst))


stringIn = input()
namelist = ["MOM","DAD"]
momDad(stringIn,namelist)