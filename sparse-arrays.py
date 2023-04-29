import math

def matchingStrings(strings, queries):
    l=[]
    for i in range(len(queries)):
        a=0
        for j in range(len(strings)):
            if strings[j]==queries[i]:
                a+=1
        l+=[a]
    return l
