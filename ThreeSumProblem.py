import random
def threesums(arr,k):


    
    indices=[]
    arr.sort()
    ans=[]
    print(arr)
    for i in range(len(arr)):
        left=i+1
        right=len(arr)-1
        
        while left<right:
            if arr[i]+arr[left]+arr[right]==k:
                
                if len(ans)==0 or (arr[i],arr[left],arr[right])!=ans[-1]:
                    ans.append((arr[i],arr[left],arr[right]))
               
                left+=1
                right-=1
            elif arr[i]+arr[left]+arr[right]<k:
                left+=1
            else:
                right-=1


    for e in ans:
        print(e)
arr=[]
for i in range(10):
    arr.append(random.randint(-10,10))
k=0
print(threesums(arr,k))