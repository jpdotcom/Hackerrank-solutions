from fractions import Fraction
ans=0
def change_root(adj,parent,u,correct,guesses,k,prev_root):
    global ans
    
    prev_correct=correct
    for v in adj[u]:
        
        if v!=prev_root:
            parent[u]=v
            parent[v]=-1
            
            if (u,v) in guesses or (v,u) in guesses:
                
                if (v,u) in guesses:
                    correct+=1
                elif (u,v) in guesses:
                    correct-=1
            
            if correct>=k:
                
                ans+=1
            
            change_root(adj,parent,v,correct,guesses,k,u)
            correct=prev_correct
            parent[v]=u
            parent[u]=-1

def getinitState(adj,correct,u,guesses,parent):
    
    for v in adj[u]:
        
        if parent[u]!=v:
            parent[v]=u
            if (u,v) in guesses:
                
                correct=getinitState(adj,correct+1,v,guesses,parent)
            
            else:
                correct=getinitState(adj,correct,v,guesses,parent)
    
    return correct



def storyOfATree(n, edges, k, guesses):
    print(n,edges,k,guesses)
    global ans
    adj={}
    for i in range(len(guesses)):
        guesses[i]=tuple(guesses[i])
    guesses=set(guesses)
    
    parent=[-1]*(n+1)
    for a,b in edges:

        if a not in adj:
            adj[a]=[]
        
        if b not in adj:
            adj[b]=[]
    
        adj[a].append(b),adj[b].append(a)
   
    correct=getinitState(adj,0,1,guesses,parent)
    if correct>=k:
        ans+=1
    change_root(adj,parent,1,correct,guesses,k,1)
    
    return str(Fraction(ans,n))

edges=[[1, 2], [1, 3]]
n=3
k=2
guesses=[[1, 2], [1, 3]]
print(storyOfATree(n,edges,k,guesses))


   


