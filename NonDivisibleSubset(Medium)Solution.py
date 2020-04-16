def freqeuncy(n,k):
    freq={}
    for i in range(len(n)):
        b=k-(n[i]%k)
      
        if b!=k :
            if b not in freq:
                freq[b]=0
            freq[b]+=1
        else:
            if 0 not in freq:
                freq[0]=0
            freq[0]+=1
        if k/2.0 in freq:
            freq[k/2]=1
   
    return freq
    

    
    
    
 

def max_frequency(x):
    max_freq=0
    max_freq_key=None
    for frequencies in x:
        if frequencies!=0:
            previous_max=max_freq
            max_freq=max(x[frequencies],max_freq)
            if previous_max!=max_freq:
                max_freq_key=frequencies
    return max_freq_key

def nonDivisibleSubset(k, s):
    mark=None
    ans=0
    frequency_func=(freqeuncy(s,k))
    maximum=max_frequency(frequency_func)
    
    if 0 in frequency_func:
        mark=1
    else:
        mark=0
    while len(frequency_func)!=mark:
       
        ans+=frequency_func[maximum]
        del frequency_func[maximum]
        if k-maximum in frequency_func:
            del frequency_func[k-maximum]
        maximum=max_frequency(frequency_func)
    if mark==1:
        ans+=1
    return ans


s=[1,2,2,3,45,5,6,7,50,104,107]  
k=2
print(nonDivisibleSubset(k,s))





            


    

