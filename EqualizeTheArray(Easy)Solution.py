def equalizeArray(arr):
    ans=0
    greatest_freq=0
    freq={}
    for number in arr:
        if number not in freq:
            freq[number]=0
        freq[number]+=1
    for key in freq:
        greatest_freq=max(greatest_freq,freq[key])
    for key in freq:
        if greatest_freq==freq[key]:
            greatest_freq=None
        else:
            ans+=freq[key]
    return ans

arr=[3,3,2,1,3]
print(equalizeArray(arr))   