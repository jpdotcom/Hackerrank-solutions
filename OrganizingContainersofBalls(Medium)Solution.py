def organizingContainers(container):
    column_sums={}
    for i in range(len(container)):
        b=0
        for j in range(len(container)):
            b+=container[j][i]
        if b not in column_sums:
            column_sums[b]=0
        column_sums[b]+=1
    for i in range(len(container)):
        c=0
        for j in range(len(container)):
            c+=container[i][j]
        if c not in column_sums or column_sums[c]==0:
            return "Impossible"
        else:
            column_sums[c]-=1
    return "Possible"
container=[[1,3,1],[2,1,2],[3,3,3]]
print(organizingContainers(container))