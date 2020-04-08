def letter_freq(s):
    freq_of_letter={}
    b=0
    for i in range(0,len(s)):
        if (i!=len(s)-1 and s[i]!=s[i+1]) or (i==len(s)-1 and s[i]==s[i-1]):
            string=s[b:i+1]
            if string[0] not in freq_of_letter:
                    freq_of_letter[string[0]]=len(string)
            else:
                if len(string)>freq_of_letter[string[0]]:
                    freq_of_letter[string[0]]=len(string)
            b=i+1
        else:
            if s[len(s)-1] not in freq_of_letter:
                 freq_of_letter[s[len(s)-1]]=1
    return freq_of_letter
              
def weighted_letter(s):
    weighted_letter_value={}
    for letter in s:
        if letter not in weighted_letter_value:
            weighted_letter_value[letter]=ord(letter)-96
    return weighted_letter_value

def max_weight(weighted_letter_value,freq_of_letters):
    letter_max_weight={}
    for letter in freq_of_letters:
        if letter not in letter_max_weight:
            #this gives the max possible value that can be produced by the string using the same letter in a range from [0,inf)
            letter_max_weight[letter]=freq_of_letters[letter]*weighted_letter_value[letter]
    return letter_max_weight

def weightedUniformStrings(s, queries):
    queries_solved={}
    queries_solved_list=[]
    letter_max=max_weight(weighted_letter(s),letter_freq(s))
    letter_weight= weighted_letter(s)

    for letter in letter_max:
        for i in range(0,len(queries)):
            if queries[i] not in queries_solved:
                queries_solved[queries[i]]="No"
            if letter_max[letter]>=queries[i] and queries[i]%letter_weight[letter]==0:
                queries_solved[queries[i]]="Yes"
            #if the final letter is reached and the quiery has yet to be solved (a.k.a be found in the dictionary)
            #The problem asks for list returned so I loop through the queries array and not the dictionary to maintain order
  
    for quiery in queries:
        queries_solved_list.append(queries_solved[quiery])
        
        
    return queries_solved_list

            
                
    
  

queries=[290290,113942,565585,788268,929914,294162,1020208,149845,408243,774403, 42119, 1755575, 178411, 390156, 1766901, 2273041, 2895849, 2006542, 134409, 1473194]
s="Insert String here"


print(letter_freq(s))

print(weightedUniformStrings(s,queries))

