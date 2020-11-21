def countLength(s):
    dic2={}

    for i in s:
        if i in dic2:
            dic2[i]+=1
        else:
            dic2[i]=1
    return len(dic2)
    
def maxSubString(s):
    strlength=len(s)

    if strlength==0 or strlength==1:
        return(strlength)
    
    up = 0
    dic = {}
    dic[s[up]] = 1
    char_max = countLength(s)
    min_element = strlength + 1
    
    for x in range(1,strlength):
        if s[x] in dic:
            dic[s[x]] += 1
        else:
            dic[s[x]] = 1

        if len(dic)==char_max:
            while up<x and dic[s[up]]>1:
                dic[s[up]]-=1
                up+=1

            if min_element>x+1-up:
                min_element = x+1-up

    return(min_element)

if __name__ == "__main__":    
    s=str(input())
    print(maxSubString(s))