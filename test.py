import sys
import time
import random
sys.setrecursionlimit(10000)
mod=10**9+7
def check(tree,tree_idx,arr,arr_idx):
    

    if tree_idx in tree:
        if arr[tree[tree_idx][0]]>=arr[arr_idx]:
            return check(tree,2*tree_idx+1,arr,arr_idx)%mod
        elif tree[tree_idx][0]<arr_idx:
            return (tree[tree_idx][1]%mod+check(tree,2*tree_idx+1,arr,arr_idx)%mod+check(tree,2*tree_idx+2,arr,arr_idx)%mod)%mod
    
    return 0

def insert(tree,val,idx,arr):
    node=arr[val[0]]
    
    if idx in tree:
        if arr[tree[idx][0]]<node:
            return insert(tree,val,2*idx+2,arr)
        else:
            return insert(tree,val,2*idx+1,arr)

    tree[idx]=val
    return
def candles(arr):
    s=time.time()
    ans=0
    tree={}
    insert(tree,(0,1),0,arr)
    for i in range(1,len(arr)):
        add=1
        add+=check(tree,0,arr,i)
        insert(tree,(i,add),0,arr)
    
    for key in tree:
        ans+=tree[key][1]
    
    return ans,time.time()-s
arr=[]
for i in range(10**4):
    arr.append(random.randint(1,10**4))

print(candles(arr))
