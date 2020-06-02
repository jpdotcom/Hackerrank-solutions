def isValid(s):
    len_freq=[0]*10**2
    letter_freq={}

    errors=0
    for letters in s:
        if letters not in letter_freq:
            letter_freq[letters]=0
        letter_freq[letters]+=1
    for letters in letter_freq:
        len_freq[letter_freq[letters]]+=1
    most_freq=len_freq.index(max(len_freq))
    print(len_freq)
    for i in range(len(len_freq)):
        if len_freq[i]!=0:
            if i!=most_freq:
                a=1 if i>most_freq else -1
                
                if len_freq[i]==1:
                    if i-most_freq==a:
                        errors+=1
                    else:
                        return "NO"
                else:
                    return "NO"
    if errors>1:
        return "NO"
    return "YES"


    
s="aaaabbcc"
print(isValid(s))