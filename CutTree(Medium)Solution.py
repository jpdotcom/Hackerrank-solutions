def getChildern(v,adj,childernof,visited):
  global parent
  visited.add(v)
  for u in adj[v]:
    if u not in visited:
      childernof[v].append(u)
      getChildern(u,adj,childernof,visited)
      parent[v]=u
  
  return
  
parent=[]
Subtrees=[]
def getSubtrees(u,edges_left,childernof,start,cuts):

  if cuts<0:
    return 0

  if start==len(childernof[u]) and cut==0 and edges_left==0:
    dp[u][edges_left][cut]:=1


  



def CutTree(edges,n,k):
  global Subtrees
  
  for i in range(n+1):
    temp=[]
    for j in range(k+1):
      temp.append([-1]*(n+1))
    Subtrees.append(temp)
  
  childernof=[]
  for i in range(n+1):
    childernof.append([])
  adj={}
  for a,b in edges:
    if a not in adj:
      adj[a]=[]
    if b not in adj:
      adj[b]=[]
    adj[a].append(b),adj[b].append(a)
    visited=set()
  getChildern(1,adj,childernof,visited)
  
  for node in childernof:
    print(node)
  return

edges=[[2,1],[2,3],[1,4],[4,5]]
n=5
k=2
CutTree(edges,n,k)
      


