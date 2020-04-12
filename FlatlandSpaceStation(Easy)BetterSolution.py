import math
def flatlandSpaceStations(n, c):
    c.sort()
    all_distances=[]
    max_distance=0
    if n!=len(c):
        for i in range(0,len(c)):
            if i!=len(c)-1 and (c[i]+1)!=c[i+1]:
                distance=math.floor((c[i+1]-c[i])/2)
                all_distances.append(distance)
        if c[0]!=0:
            all_distances.append(c[0])
        if c[len(c)-1]!=n-1:
            all_distances.append((n-1)-c[len(c)-1])
    
    for distances in all_distances:
        max_distance=max(max_distance,distances)
    return max_distance
n=5
c=[0,4]

print(flatlandSpaceStations(n,c))
                