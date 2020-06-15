cuts=0
def is_evenorodd(x,y):
    if (x%2==0 and y%2==0) or (x%2==1 and y%2==1):
        return True
    return False

def create_tree(edges):
    tree={}
    for i in range(len(edges)):
        if edges[i][0] not in tree:
            tree[edges[i][0]]=[]
        if edges[i][1] not in tree:
            tree[edges[i][1]]=[]
        tree[edges[i][0]].append(edges[i][1])
        tree[edges[i][1]].append(edges[i][0])
    return tree



def subtree_sum(tree,node,subtrees,indices):
    global cuts
    x=1
    indices.add(node)
    for i in range(len(tree[node])):
        if tree[node][i] not in indices:
            
            x+=subtree_sum(tree,tree[node][i],subtrees,indices)
    if x%2==0:
        cuts+=1
        x=0
    subtrees[node]=x
    return x
    

def evenForest(t_nodes, t_edges, t_from, t_to):
    edges=[]
    for i in range(len(t_from)):
        edges.append([t_from[i],t_to[i]])
    tree=create_tree(edges)
    node=1
    subtrees={}
    indices=set([])
    ans=0
    subtree_sum(tree,node,subtrees,indices)

    return cuts-1
           
            
            




    