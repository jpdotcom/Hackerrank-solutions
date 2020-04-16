def maximumSum(a, m):
    max_mod_one=0
    max_mod_two=0
    
    arr_sum_mod=[]
    b=a[0]
    for i in range(0,len(a)):
        
        if i==0:
            num_index=b%m,i
           
            arr_sum_mod.append(num_index)
           
        else:
            b+=a[i]
            num_index=b%m,i
            arr_sum_mod.append(num_index)
           
    arr_sum_mod.sort(key=lambda x:x[0])
    for i in range(1,len(arr_sum_mod)):
        
        left=arr_sum_mod[i-1][0]
        right=arr_sum_mod[i][0]
        if arr_sum_mod[i-1][1]>arr_sum_mod[i][1] and left!=right:
                
            max_mod_two=max(max_mod_two,(m-abs(left-right)))
    for i in range(len(arr_sum_mod)):
        max_mod_one=max(max_mod_one,arr_sum_mod[i][0])
    return max(max_mod_one,max_mod_two)
        
            
    
    

a=[3,3,9,9,5]
m=7
print(maximumSum(a,m))