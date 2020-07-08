def traverse_astronaunts(adj,vertices,node):
    
    for i in range(len(adj[node])):
        
        if adj[node][i] not in vertices:
            
            vertices.add(adj[node][i])
            traverse_astronaunts(adj,vertices,adj[node][i])
    return len(vertices)
    
def journeyToMoon(n, astronaut):
    adj_list={}

    for i in range(len(astronaut)):
        a,b=astronaut[i]

        if a not in adj_list:
            adj_list[a]=[]

        if b not in adj_list:
            adj_list[b]=[]

        adj_list[a].append(b),adj_list[b].append(a)
    
    vertices=set([])
    component_list=[]
    for node in adj_list:
        
        if node not in vertices:
            
            prev_len=len(vertices)
            vertices.add(node)
            
           
            new_len=traverse_astronaunts(adj_list,vertices,node)
            
            component_list.append((new_len-prev_len))
    
    for i in range(n-len(vertices)):
        component_list.append(1)
    
    res=0
    component_sum=sum(component_list)
    print(component_list)
    for i in range(len(component_list)):
        component_sum-=component_list[i]
        res+=component_sum*component_list[i]
    return res

astronaut=[[1,2],[2,3]]
n=4
print(journeyToMoon(n,astronaut))


