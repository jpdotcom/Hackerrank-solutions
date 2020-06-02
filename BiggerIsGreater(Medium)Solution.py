lexographic_key_reverse={1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
lexographic_key={'l': 12, 'j': 10, 'o': 15, 'i': 9, 'c': 3, 'n': 14, 'm': 13, 'v': 22, 't': 20, 'r': 18, 's': 19, 'q': 17, 'g': 7, 'y': 25, 'u': 21, 'z': 26, 'd': 4, 'p': 16, 'a': 1, 'k': 11, 'x': 24, 'e': 5, 'f': 6, 'w': 23, 'h': 8, 'b': 2}
def str_to_list(w):
    x=[]
    for i in range(len(w)):
        x.append(lexographic_key[w[i]])
    print(x)
    return x
def list_to_str(w_list):
    w=[]
    for i in range(len(w_list)):
        w.append(lexographic_key_reverse[w_list[i]])
    return "".join(w)      
def last_idx(w_list):
    idx={}
    for i in range(len(w_list)):
        idx[w_list[i]]=i
    return idx
def biggerisGreater(w):
    w_list=str_to_list(w)
    last=last_idx(w_list)
    print(last)
    indices=None
    for i in range(len(w_list)):
        x=w_list[i]+1
        found=True
        while (x not in last) or (last[x]<i):
            if x>=26:
                
                found=False
                break
            x+=1
        if found:
            indices=(i,last[x])
    
    if indices==None:
        return "no answer"
    i,j=indices
    prev_val=w_list[i]
    w_list[i]=w_list[j]
    w_list[j]=prev_val
    first=w_list[0:i+1]
    second=w_list[i+1:len(w_list)]
    second.sort()
    res=first+second
    return list_to_str(res)


w="abc"
print(biggerisGreater(w))
    

    