import math

def chocolateFeast(n, c, m):
    bars=math.floor(n/c)
    total_bars=bars
    wrappers=0
    while (bars+wrappers)%m!=bars+wrappers:
        previous_bars=bars
        bars=math.floor((bars+wrappers)/m)
        wrappers=(previous_bars+wrappers)%m
        total_bars+=bars
  
    return int(total_bars)

n=6
c=2
m=2
print(chocolateFeast(n,c,m))
