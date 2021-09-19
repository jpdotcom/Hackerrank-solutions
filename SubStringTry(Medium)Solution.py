def substringDiff(k,s1,s2):
    dp=[]
    for i in range(len(s1)):
        temp=[]
        for j in range(len(s2)):
            temp.append((s1==s2))
        dp.append(temp)
    ans=0
    
    for i in range(len(s1)):
        s1_front=i 
        s2_front=0
        s2_back=0
        s1_back=i
        invariants=0
        while s1_front<len(s1) and s2_front<len(s2):
            print(s1_front,s1_back,s2_front,s2_back)
            if not dp[s1_front][s2_front]:
                invariants+=1
            
            if invariants>k:
                while invariants>k and s1_back<s2_front and s2_back<s2_front:
                    if not dp[s1_back][s2_back]:
                        invariants-=1
                    s1_back+=1
                    s2_back+=1

            ans=max(s2_front-s2_back,ans)
            s1_front+=1
            s2_front+=1
        

    return ans
s1="torino"
s2="tabriz"
k=2
print(substringDiff(k,s1,s2))