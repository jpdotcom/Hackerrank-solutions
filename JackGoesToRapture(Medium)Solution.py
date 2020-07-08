import heapq
def traverse_stations(adj,edge_weights,n,vertex_sum):
    seen=set([])
    vertex_weights={1:0}
    for i in range(2,n+1):
        vertex_weights[i]=float('inf')
    
    while len(vertex_sum)!=0:
        
        
        vertex_weight,node=heapq.heappop(vertex_sum)

        if node not in seen:
            seen.add(node)

            next_nodes=adj[node]

            
            for i in range(len(next_nodes)):
                edge=(node,next_nodes[i])
                if edge not in edge_weights:
                    edge=(edge[1],edge[0])
                
                edge_weight=edge_weights[edge]
                
                
                if next_nodes[i] not in seen:
                    
                    if vertex_weight<edge_weight:
                        vertex_weights[next_nodes[i]]=min(edge_weight,vertex_weights[next_nodes[i]])
                    else:
                        vertex_weights[next_nodes[i]]=min(vertex_weights[next_nodes[i]],vertex_weight)
                    

                    heapq.heappush(vertex_sum,(vertex_weights[next_nodes[i]],next_nodes[i]))
            
    return vertex_weights[n]