def power(k):
    

    if 2**k/k==int(2**k/k):
        return 2**k/k
    else:
        return str(k)+" is not a valid solution"
for i in range(1,100):
    print(power(i))