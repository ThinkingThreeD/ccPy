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
   smooth(min, max, a)            - Ease-in ease-out curve
   smooth(min, max, a, roll)      - Ease-in ease-out curve (with rolloff)
   lerp(v1, v2, t)                - Linear interpolation
   fit(val, omin,omax, nmin,nmax) - Map val in (oldmin,oldmax) to (newmin,newmax)

SOURCES:
lerp
   http://www.sidefx.com/docs/hdk15.0/_s_y_s___math_8h_source.html
   line 627
clamp
   http://www.sidefx.com/docs/hdk15.0/_math_8h_source.html
   line 232
fit
   http://www.sidefx.com/docs/hdk15.0/_s_y_s___math_8h_source.html
   line 759
fit01
   http://www.sidefx.com/docs/hdk15.0/_s_y_s___math_8h_source.html
   line 797

'''
  
def lerp(v1,v2, t):
    return v1 + (v2 - v1)*t 
    
    
def clamp(val, min, max):
   '''
   --------------------------------
   if val < min:
      return min
   elif val > max:
      return max
   else:
      return val
   ---------------------------------
   if val < min: return min
   elif val > max: return max
   else:return val
   --------------------------------
   '''
   return min if val < min else max if val > max else val

def fit(val , oldmin , oldmax , newmin , newmax):
   '''
   Remaps the value from the old range to the new range and clamps it
   '''
    d = oldmax - oldmin
    if (oldmin < oldmax):
        if (val < oldmin): 
            return newmin
        if (val > oldmax): 
            return newmax
    else:
        if (val < oldmax):
            return newmax
        if (val > oldmin):
            return newmin
    return newmin + (newmax-newmin)*(val-oldmin)/d

def fit01(val, minVal, maxVal):
   '''
   Just like fit() but assumes value is already in the range 0 to 1.
   '''
    if (val < 0) : return minVal
    if (val > 1): return maxVal
    return lerp(minVal, maxVal, val)
    
if __name__ == '__main__':
  print clamp(45,0,6)
  print fit(30 , 0 , 90 , 0 , 1)
