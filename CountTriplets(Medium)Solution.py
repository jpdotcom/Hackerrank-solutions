import random
import time
def countTriplets(arr,r):
  start=time.time()
  freq_1={}
  freq_2={}
  freq_3={}

  for i in range(len(arr)):
    
    #Third
    if arr[i]%r==0 and arr[i]>=r**2:
      a,b,c=arr[i]/(r**2),arr[i]/r,arr[i]

      if (a,b,c) not in freq_3:
        freq_3[(a,b,c)]=0
      
      if (a,b) not in freq_2:
        freq_2[(a,b)]=0
      
      freq_3[(a,b,c)]+=freq_2[(a,b)]
    
    #Second
    if arr[i]%r==0 and arr[i]>=r:
      
      b,c=arr[i]/r,arr[i]

      if (b,c) not in freq_2:
        freq_2[(b,c)]=0
      if b not in freq_1:
        freq_1[b]=0
      
      freq_2[(b,c)]+=freq_1[b]
    
    #First
    if arr[i] not in freq_1:
      freq_1[arr[i]]=0
    
    freq_1[arr[i]]+=1
    
    
    
  ans=0
  for key in freq_3:
    ans+=freq_3[key]
  return ans,time.time()-start,len(freq_1)+len(freq_2)+len(freq_3)

arr=[]
for i in range(10**5):

  arr.append(random.randint(1,10**9+1))

r=random.randint(1,10**9+1)
print(countTriplets(arr,r))