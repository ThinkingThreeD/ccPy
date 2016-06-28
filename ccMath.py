'''
Copyright (c) 2016 ThinkingTreeD

Interpolation/Range:
   clamp(val, min, max)           - Clamp value between min and max
   smooth(min, max, a)          - Ease-in ease-out curve
   smooth(min, max, a, roll)    - Ease-in ease-out curve (with rolloff)
   Slerp(v1, v2, bias)           - Linear interpolation
   fit(v, omin,omax, nmin,nmax) - Map v in (omin,omax) to (nmin,nmax)
  
'''

def clamp(val, mini, maxi):
    if val<mini:
        val = mini
    elif val > maxi:
        val = maxi
    return val


    
if __name__ == '__main__':
  print clamp(45,0,6)
