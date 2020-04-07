def serviceLane(cases, width):
    minimum=1000
    ans=[]
    for i in range(0,len(cases)):
        start_end=cases[i]
        for j in range(start_end[0],start_end[1]+1):
            minimum=min(minimum,width[j])
        ans.append(minimum)
        minimum=1000
    return ans

width=[2 ,3, 1, 2, 3, 2, 3, 3]   
cases=[[0,3], [ 4, 6] ,[6 ,7] ,[3 ,5] ,[0, 7]]
print(serviceLane(cases,width))