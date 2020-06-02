from collections import defaultdict
import sys
def SmallestSubString (S):
  c=len(set(list(S)))#count
  n=len(S)
  freq=defaultdict(int)
  i=0 #start of Index
  minlen=sys.maxsize
  c1=0 
  for j in range(n):
    freq[S[j]]+=1
    if freq[S[j]]==1:
      c1+=1
    if c==c1:
      while freq[S[i]]>1:
        if freq[S[i]]>1:
          freq[S[i]]-=1
        i+=1
      currlen = j-i+1
      minlen=min(minlen, currlen)
  return minlen
 
    
S = input() 
output=SmallestSubString(S)
print (output)
