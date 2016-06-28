'''
COPYRIGHT:
   2016 ThinkingTreeD
   cyrill.calbac@gmail.com
   0033715683949
   France
NAME: 
   ccMath.py
COMMENTS:
   3d Math python module 
   
FUNCTIONS:
   clamp(val, min, max)           - Clamp value between min and max
   smooth(min, max, a)          - Ease-in ease-out curve
   smooth(min, max, a, roll)    - Ease-in ease-out curve (with rolloff)
   Slerp(v1, v2, bias)           - Linear interpolation
   fit(v, omin,omax, nmin,nmax) - Map v in (omin,omax) to (nmin,nmax)
  
'''

def clamp(val, min, max):
   if val < min:
      return min
   elif val > max:
      return max
   else:
      return val


    
if __name__ == '__main__':
  print clamp(45,0,6)
