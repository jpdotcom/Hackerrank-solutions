import random
def isMagicSquare(n):
    b=n[0][0]+n[1][0]+n[2][0]
    if b==n[0][1]+n[1][1]+n[2][1] and b==n[0][2]+n[1][2]+n[2][2] and b==n[0][0]+n[0][1]+n[0][2] and b==n[1][0]+n[1][1]+n[1][2] and b==n[2][0]+n[2][1]+n[2][2] and b==n[0][0]+n[1][1]+n[2][2] and b==n[0][2]+n[1][1]+n[2][0]:
        return True
    return False

def magicsquare():
    temp_row=[]
    square_consider=[]
    permuatations=10*9*8*7*6*5*4*3*2*1
    magic_squares=[]
    
    integers_to_chose=[1,2,3,4,5,6,7,8,9]
    while permuatations!=0:
        for i in range(3):
            for j in range(3):
                x=random.choice(integers_to_chose)
                temp_row.append(x)
                integers_to_chose.remove(x)
            square_consider.append(temp_row)
            temp_row=[]
       
        consider=isMagicSquare(square_consider)
        if consider:
            if square_consider not in magic_squares:
                magic_squares.append(square_consider)
            else:
                permuatations+=1
            
        
        permuatations-=1
        integers_to_chose=[1,2,3,4,5,6,7,8,9]
        square_consider=[]
    return magic_squares

print(magicsquare())
            

        
        