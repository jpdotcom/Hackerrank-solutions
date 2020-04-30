def pairs(k, arr):
    ans=0
    arr.sort()
    
    arr_set=set(arr)
  
    for i in range(len(arr)):
        if arr[i] in arr_set:
            x=arr[i]
            while x in arr_set:
                if x+k in arr_set:
                    arr_set.remove(x)
                    x+=k
                    ans+=1
                else:
                    break
    return ans

k=2
arr=[363374326, 364147530, 61825163 ,1073065718 ,1281246024 ,1399469912 ,428047635, 491595254, 879792181 ,1069262793]
print(pairs(k,arr))