def freq(arr):
    frequency=[0]*(2*10**4)
    for integer in arr:
        frequency[integer]+=1
    return frequency


def beautifulTriplets(d,arr):
    freq_=freq(arr)
    all_possible_triplets=0
    arr_set=set(arr)
    for integer in arr_set:
        if (integer+d) in arr_set:
            b=integer+d
            if b+d in arr_set:
                times_to_add=(freq_[integer]*freq_[b]*freq_[b+d])
                all_possible_triplets+=times_to_add
                    

return all_possible_triplets