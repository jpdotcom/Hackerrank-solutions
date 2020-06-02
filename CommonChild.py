import copy
def indices_dic(letters):
    indices={}
    for i in range(len(letters)):
        if letters[i] not in indices:
            indices[letters[i]]=[i]
        else: 
            indices[letters[i]].append(i)
    print(indices)
    return indices



def commonChild(s1,s2):
    lengths=[0]
    s2_dictionary=indices_dic(s2)
    for i in range(len(s1)):
        
        if s1[i] in s2_dictionary:
            
            markers=[]
            idx=0
            temp_letters=[]
            copy_dic=copy.deepcopy(s2_dictionary)
            for j in range(i,len(s1)):
                
                temp_letters.append(s1[j])
                
                if (s1[j] not in copy_dic)  or  (len(copy_dic[s1[j]])==0) or (len(markers)>=1 and (copy_dic[s1[j]][0])<markers[idx-1]):
                 
                    temp_letters.pop(len(temp_letters)-1)
                    copy_dic[s1[j]].pop(0)
               
                

                else:    
                    
                    markers.append(copy_dic[s1[j]][0])
                    idx+=1
                    copy_dic[s1[j]].pop(0)
                if len(temp_letters)==0:
                    break
                
            print(temp_letters)
            print (markers)
            lengths.append(len(temp_letters))
            markers=[]
            idx=0
            temp_letters=[]
        
    return max(lengths)
            
    
                    
s1="OWWWOB"
s2="OXOXWWWOB"

print(commonChild(s1,s2))
