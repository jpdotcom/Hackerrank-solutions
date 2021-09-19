def intervalSelection(intervals):
  intervals.sort(key=lambda x:(x[1],x[0]))
  ans=[intervals[0]]
  idx=1
  limit=0
  while idx<len(intervals):
    ans.append(intervals[idx])
    
    if ans[-2][1]>=ans[-1][0]:
      if limit>=ans[-1][0]:
        ans.pop()
      else:
        limit=ans[-2][1]
    
    idx+=1
    
  return len(ans)