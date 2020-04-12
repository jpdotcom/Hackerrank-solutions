def num_to_binary(n):
    binary=[]
    num_to_switch=n
    x=0
    
    largest_num=1
    while num_to_switch!=0:
        if num_to_switch==n:
            if largest_num<=num_to_switch:
                x+=1
                largest_num*=2
            else:
                
                largest_num/=2
                num_to_switch-=largest_num
                binary.append("1")
                
                largest_num/=2
                x-=2
        else:
            if largest_num>num_to_switch:
                largest_num/=2
                binary.append("0")
                x-=1
            else:
                binary.append("1")
                num_to_switch-=largest_num
                largest_num/=2
                x-=1
    b=x+1
    for i in range(b):
        x-=1
        binary.append("0")
    return binary

def sumXor(n):
    if n==0:
        return 1
    num_Zero=0
    index_sub=None
    binary_string=num_to_binary(n)
    for i in range(0,len(binary_string)):
        if binary_string[i]=="1":
            index_sub=i 
            break
    binary_string=binary_string[index_sub:len(binary_string)]
    for numbers in binary_string:
        if numbers=="0":
            num_Zero+=1
    return (2**num_Zero)
n=1
print(sumXor(n))



            
