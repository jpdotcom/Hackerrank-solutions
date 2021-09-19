import time
mod=10**9+7
import sys
sys.setrecursionlimit(10000)
def exp(base,exponent):
    
    if exponent==1:
        return base
    
    elif exponent & 1:
        
        return (base%mod*exp((base%mod*base%mod)%mod,(exponent//2)))%mod
    
    return exp((base%mod*base%mod)%mod,exponent//2)

def normal(base,exponent):
    
    return base**exponent


exponent=10**879
print(exp(2,exponent))



