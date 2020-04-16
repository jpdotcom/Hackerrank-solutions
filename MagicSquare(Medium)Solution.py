import random
pre = [
            [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
            [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
            [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
            [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
            [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
            [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
            [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
            [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
            ]
def formingMagicSquare(s):
    ans=100000000
    acuracay=[]
    temp_acuracay=0
    for magic_square in pre:
        for j in range(0,3):
            for k in range(0,3):
                
                temp_acuracay+=abs(s[j][k]-magic_square[j][k])
                
        acuracay.append(temp_acuracay)
        temp_acuracay=0
    for integer in acuracay:
        ans=min(ans,integer)
    return ans

s=[[4,9,2],[3,5,7],[8,1,5]]
print(formingMagicSquare(s))
        

        