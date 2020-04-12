def no_spaceships(n,c):
    null_spaceships=[]
    for i in range(0,n):
        null_spaceships.append(i)
    for i in range(0,len(c)):
        null_spaceships.remove(c[i])
    return null_spaceships


def flatlandSpaceStations(n, c):
    all_distances=[0]
    min_distance=10**5
    max_distance=0
    null_spaceships=no_spaceships(n,c)
    for city in null_spaceships:
        for spaceships in c:
            min_distance=min(min_distance,abs(city-spaceships))
        all_distances.append(min_distance)
        min_distance=10**5
    for distance in all_distances:
        max_distance=max(max_distance,distance)
    return max_distance
n=6
c=[0,1,2,3,4,5]
print(flatlandSpaceStations(n,c))

    