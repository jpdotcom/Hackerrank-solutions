def howManyGames(p, d, m, s):
    games_bought=0
    while s>=0:
        games_bought+=1
        if p>=m:
            s-=p
            p-=d 
        else:
            s-=m
        
    return (games_bought-1)
p=20
d=3
m=6
s=85
print(howManyGames(p,d,m,s))
    