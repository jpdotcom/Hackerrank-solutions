def summingPieces(arr):
    

    dp=[0 for i in range(len(arr))]

    prefix=[arr[0]]
    big_sum=[prefix[0]]
    for i in range(1,len(arr)):
        
        prefix.append(prefix[-1]+arr[i])
    for i in range(1,len(prefix)):
        big_sum.append(big_sum[i-1]+(2**i)*(i)*arr[i])
    left_sum=0
    right_sum=0
    
    for i in range(len(dp)):
        if i==0:
            dp[i]=arr[0]
        else:
            print(left_sum+right_sum)
            dp[i]=left_sum+right_sum
        
        if i!=len(dp)-1:    
            left_sum+=dp[i]
            right_sum+=big_sum[i]
            right_sum+=(((i+1)*(i+2))/2-1)*arr[i+1]
            
            
       
            
        
        
        
    return dp

print(summingPieces([4,2,9,10,1]))