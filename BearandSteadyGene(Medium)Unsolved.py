def isValid(freq,n):
    check=n/4
    
    if freq["A"]<=check and freq["C"]<=check and freq['G']<=check and freq["T"]<=check:
        return True
    return False
        
def steadyGene(gene):
    freq={"A":0,"C":0,"G":0,"T":0}
    i=0
    j=len(gene)-1
    n=len(gene)
    while True:
        letter=gene[i]
        freq[letter]+=1
        
        if isValid(freq,n) and i!=len(gene)-1:
            i+=1
            
            pass
        else:
            freq[letter]-=1
            break
    print(i,freq)
    while True:
        letter=gene[j]
        freq[letter]+=1
        if isValid(freq,n) and i<j:
            j-=1
            pass
        else:
            break
    
    return j-i+1
gene="TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"
print(steadyGene(gene),gene[28:39])