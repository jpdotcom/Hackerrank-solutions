import math

def create_squares(p, q):
    all_squares={}
    for i in range(p,q+1):
        if i not in all_squares:
            all_squares[i]=i**2
    return all_squares
def kaprekar_finder(all_squares):
    kaprekar_numbers=[]
    for integer in all_squares:
        integer_str=str(integer)
        sqaure_str=str(all_squares[integer])
        
        if len(integer_str)!=len(sqaure_str):
            left_of_square=int(float(sqaure_str[0:(len(sqaure_str)-len(integer_str))]))
            right_of_square=int(float((sqaure_str[(len(sqaure_str)-len(integer_str)):len(sqaure_str)+1])))
            
            if (left_of_square + right_of_square)==integer:
                kaprekar_numbers.append(integer)
        elif integer==1:
            kaprekar_numbers.append(integer)
    
    return(', '.join(map(str, kaprekar_numbers)))
        
        
    
    
        

p=400
q=700
s="abcd"
print(s[len(s)-1])
print(len(kaprekar_finder((create_squares(p,q)))))


        
    
