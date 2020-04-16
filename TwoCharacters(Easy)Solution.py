def all_unique_letters(s):
    letter=[]
    letters=set(letter)
    for string in s:
        if string not in letters:
            letters.add(string)
    return letters  

def alternate(s):
    final_ans=0
    answers=[]
    letters_in_s=list(all_unique_letters(s))
    i=0
    j=i+1
    while i!=len(letters_in_s)-1:
        copy_str=list(s)
        copy_str=[x for x in copy_str if x==letters_in_s[i] or x==letters_in_s[j] ]
        for b in range(0,len(copy_str)-1):
            if copy_str[b]==copy_str[b+1]:
                break
            elif b==len(copy_str)-2:
                answers.append(len(copy_str))
        if j==len(letters_in_s)-1:
            i+=1
            j=i+1
        else:
            j+=1
    for lengths in answers:
        final_ans=max(final_ans,lengths)
    return final_ans
s="insertstringhere"
print(alternate(s))

