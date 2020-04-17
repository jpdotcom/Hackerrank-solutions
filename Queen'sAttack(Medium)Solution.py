def queensAttack(n, k, r_q, c_q, obstacles):
    ans=0
    for i in range(len(obstacles)):
        obstacles[i]=tuple(obstacles[i])
    obstacles=set(obstacles)
    
   

    right=c_q+1
    left=c_q-1
    up=r_q+1
    down=r_q-1
    x=r_q+1
    y=c_q-1
    w=r_q-1
    z=c_q+1
    a=r_q-1
    b=c_q-1
    c=r_q+1
    d=c_q+1


    neg_slop_down=x,y
    neg_slop_up=w,z
    pos_slop_down=a,b
    pos_slop_up=c,d
    while right!=n+1:
        
        if (r_q,right) in obstacles:
            break
        else:
            right+=1
            ans+=1
    

    print(ans)
    while left!=0:
        if (r_q,left) in obstacles:
            break
        else:
            left-=1
            ans+=1
    print(ans)
    while up!=n+1:
        if (up,c_q) in obstacles:
            break
        else:
            up+=1
            ans+=1
    print(ans)
    while down!=0:
        if (down,c_q) in obstacles:
            break
        down-=1
        ans+=1
    print(ans)
    while neg_slop_up[0]!=0 and neg_slop_up[1]!=n+1:
        if (neg_slop_up) in obstacles:
            break
        else:
            ans+=1
            w-=1
            z+=1
            neg_slop_up=w,z
    print(ans)
    while neg_slop_down[0]!=n+1 and neg_slop_down[1]!=0:
        if (neg_slop_down) in obstacles:
          
            break
        else:
            ans+=1
            x+=1
            y-=1
            neg_slop_down=x,y
    
    print(ans)    
        
    while pos_slop_down[0]!=0 and pos_slop_down[1]!=0:
        if (pos_slop_down) in obstacles:
            break
        else:
            ans+=1
            a-=1
            b-=1
            pos_slop_down=a,b
    print(ans)
    while pos_slop_up[0]!=n+1 and pos_slop_up[1]!=n+1:
        if (pos_slop_up) in obstacles:
            break
        else:
            c+=1
            d+=1
            pos_slop_up=c,d
            ans+=1
    
    print(ans)

 
    return ans

k=0
obstacles=[[4,3],[5,5],[4,2],[2,3]]
n=5
r_q=4
c_q=3
print(queensAttack(n,k,r_q,c_q,obstacles))   
    
       

