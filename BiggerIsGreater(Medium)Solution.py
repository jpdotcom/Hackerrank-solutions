lexographic_key_reverse={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
lexographic_key={'l': 12, 'j': 10, 'o': 15, 'i': 9, 'c': 3, 'n': 14, 'm': 13, 'v': 22, 't': 20, 'r': 18, 's': 19, 'q': 17, 'g': 7, 'y': 25, 'u': 21, 'z': 26, 'd': 4, 'p': 16, 'a': 1, 'k': 11, 'x': 24, 'e': 5, 'f': 6, 'w': 23, 'h': 8, 'b': 2}

def biggerIsGreater(w):
    num_list=[]
    key=lexographic_key_reverse
    num_conversion=lexographic_key
    for letters in w:
        num_list.append(num_conversion[letters])
    prev_index=None
    i = len(num_list)-1
    j=i-1
    distance=-1
    str_converision=[]
    indexs=i
    checker=None
    while i!=0:
        
        while j>=0:
            
            if num_list[i]>num_list[j]:
                

                prev_index=distance
                distance=max(distance,j)
               
                if prev_index!=distance:
                    indexs=i


                checker=":D"

            j-=1
        
        i-=1
        j=i-1
    
    if checker==None:
        return "no answer"


    prev_i=num_list[indexs]
    num_list[indexs]=num_list[distance]
    num_list[distance]=prev_i
    

            
    part_to_sort=num_list[distance+1:len(num_list)]
    other_part=num_list[0:distance+1]
    part_to_sort.sort()
    final_sorted=other_part+part_to_sort
    for number in final_sorted:
        str_converision.append(key[number])
    return "".join(str_converision)


w="dkhc"
print(biggerIsGreater(w))

    