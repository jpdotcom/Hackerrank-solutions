def substringDiff(k, s1, s2):
    ans=0
    for i in range(len(s1)):
        chances=k
        j=i
        substr_len=0
        while j<=len(s1)-1:
            if s1[j]!=s2[j]:
                chances-=1
            if chances<0:
                break
            j+=1
            substr_len+=1
        ans=max(ans,substr_len)
    return ans
s1="tabriz"
s2="torino"
k=2
print(substringDiff(k,s1,s2))