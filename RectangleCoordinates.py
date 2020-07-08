#given coordinates (x,y) find and return the rectangle that has the greatest area formed by those coordinates
import math

def findLargestRectangle(coordinates):
    n=0
    final_coordinates=[]
    ans=0
    set_coords=set(coordinates)
    for i in range(len(coordinates)):
        for j in range(i+1,len(coordinates)):
            
            x1,y1=coordinates[i]

            x2,y2=coordinates[j]            #assume that line formed by these two points are the diagnols of a rectangle

            diagonl_dist=math.sqrt((x2-x1)**2+(y2-y1)**2)/2

            rectangle=set([(coordinates[i],coordinates[j])])

            for k in range(len(coordinates)):
                
                if coordinates[k] not in rectangle:
                    

                    midpoint=((x1+x2)/2,(y1+y2)/2)

                    a,b=midpoint

                    c,d=coordinates[k]

                    second_dist=math.sqrt((a-c)**2+(b-d)**2)

                    if second_dist==diagonl_dist:
                        
                        last_point=(2*a-c,2*b-d)
                        if last_point in set_coords:
                            prev_ans=ans
                            base=math.sqrt((x1-c)**2+(y1-d)**2)
                            height=math.sqrt((x2-c)**2+(y2-d)**2)

                            ans=max(ans,base*height)
                            if ans!=prev_ans:
                                final_coordinates=[(coordinates[i]),coordinates[j],coordinates[k],last_point]

    return ans,final_coordinates


coordinates=[(-3,4),(4,3),(0,0),(1,7),(8,6),(5,10)]
print(findLargestRectangle(coordinates)) 