def superReducedString(s):
    s=list(s)
    i=len(s)-1
    
    while i>0:
        
        if s[i]==s[i-1]:
            s.pop(i)
            s.pop(i-1)
            i=len(s)-1
        else:
            i-=1
    a="".join(s)
    return a if len(a)!=0 else "Empty String"

s="aaabccddd" 
print(superReducedString(s)) 