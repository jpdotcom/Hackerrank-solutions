def product_sum(arr,k):
    arr.sort()
    dp=[0]*(len(arr)+1)
    s=sum(arr)
    prev_s=s
    second=0
    for i in range(len(arr)):
        s-=arr[i]
        second+=(s)*arr[i]
    dp[0]=second
    s=prev_s

    for i in range(1,len(arr)):
        s-=arr[i-1]
        dp[i]=dp[i-1]-(arr[i-1]*s)
    
    s=prev_s
    ans=0
    for i in range(len(arr)):
        s-=arr[i]
        prev_s=s
        for j in range(i+1,len(arr)):

            s-=arr[j] 
             
            ans+=(s)*arr[i]*arr[j]
        s=prev_s
    p=0
    new_arr=[ans]
    for i in range(k):
        
        if arr[p]>0:
            arr[p]-=1
            
        elif p!=len(arr)-1:
            p+=1
            arr[p]-=1            
        ans-=dp[p+1]
        new_arr.append(ans)
    
    return new_arr

def knapsack(n,total_weight,v,second):
  dp=[[float('inf')]*(n+1) for i in range(n+1)]
  print(second)
  dp[0][0]=0
  for i in range(1,len(dp)):
    for j in range(len(dp[0])):
        for k in range(0,min(int(j/v[i-1]+1),n+1)):
            val,weight=second[i-1][k],v[i-1]
            print(val,weight)
            if j>=k:
                dp[i][j]=min(dp[i][j],val+dp[i-1][j-k])
                
            dp[i][j]=min(dp[i-1][j],dp[i][j])
  print(dp)
  return dp[-1][-1]

def main(v,lines,colors,k):

    d=[None]*(colors+1)
    dp1=[]
    for i in range(len(lines)):

        a,b,color=lines[i]
        if not d[color]:
            d[color]={}
        if a not in d[color]:
            d[color][a]=0
        d[color][a]+=1
    for i in range(1,len(d)):
        arr=[]
        for key in d[i]:
            arr.append(d[i][key])
        dp1.append(product_sum(arr,len(lines)))
    print(knapsack(len(dp1),k,v,dp1))
    return

arr=[[1,10,1],[1, 14, 2],[6 ,4, 1],[2 ,2 ,1],[0,12,2],[2,11,2],[0,6,1]]
v=[8,10]
print(main(v,arr,len(v),13))