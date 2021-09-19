def stockmax(prices):
  maxReturn=prices[-1]
  i=len(prices)-1
  ans=0
  while i!=-1:
    if maxReturn>prices[i]:
      ans+=maxReturn-prices[i]
    maxReturn=max(maxReturn,prices[i])
    i-=1
  return ans
