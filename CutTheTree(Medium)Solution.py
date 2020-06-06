def create_graph(edges):
    graph={}
    for i in range(len(edges)):
        i,j=edges[i]
        if i not in graph:
            graph[i]=[]
        if j not in graph:
            graph[j]=[]
        graph[i].append(j)
        graph[j].append(i)
    return graph
def create_sum(graph,node_sum,node,visited,data):
    visited.add(node)
    node_list=graph[node]
    x=data[node-1]
    for i in range(len(node_list)):
        if node_list[i] not in visited:
            x+=create_sum(graph,node_sum,node_list[i],visited,data)
    node_sum[node]=x
    return x
def cutTheTree(data,edges):
    graph=create_graph(edges)
    node_sum={}
    node=1
    visited=set([])
    total_sum=sum(data)
    print(create_sum(graph,node_sum,node,visited,data))
    print(node_sum)
    ans=total_sum
    for i in range(len(edges)):
        j=edges[i][1]
        ans=min(ans,abs(total_sum-(2*node_sum[j])))
    return ans


edges=[[1,2],[2,3],[2,5],[4,5],[5,6]]   

data=[100, 200, 100, 500, 100, 600]
print(cutTheTree(data,edges))

