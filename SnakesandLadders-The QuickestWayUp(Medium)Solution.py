from queue import Queue
def traverse_board(snakes,ladders):
    q=Queue(maxsize==101)
    q.put(1)
    visited={1:0}
    while q.qsize()!=0:
        pos=q.get()
        if pos in snakes:
            pos=snakes[pos]
        if pos in ladders:
            pos=snakes[pos]
        if pos==100:
            return visited[pos]
        x=visited[pos]
        if pos+1 not in visited and pos+1<=100:
            q.put(pos+1)
            visited[pos+1]=1+x
        if pos+2 not in visited and pos+2<=100:
            q.put(pos+2)
            visited[pos+2]=1+x
        if pos+3 not in visited and pos+3<=100:
            q.put(pos+3)
            visited[pos+3]=1+x
        if pos+4 not in visited and pos+4<=100:
            q.put(pos+4)
            visited[pos+4]=1+x
        if pos+5 not in visited and pos+5<=100:
            q.put(pos+5)
            visited[pos+5]=1+x
        if pos+6 not in visited and pos+6<=100:
            q.put(pos+6)
            visited[pos+6]=1+x
def quickestWayUp(ladders, snakes):
    dict1={}
    dict2={}
    for i in range(len(ladders)):
        dict1[ladders[i][0]]=dict1[ladders[i][1]]
    for i in range(len(snakes)):
        dict2[snakes[i][0]]=dict2[snakes[i][1]]
    return traverse_board(dict2,dict1)

        
        