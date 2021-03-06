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

def equalZero(a, tol=0.00001):
    return a >= -tol and a <= tol

def lerp(v1,v2, t):
    '''linear interpolation'''
    return v1 + (v2 - v1)*t 

def fit(val , oldmin , oldmax , newmin , newmax):
    '''    Remaps the value from the old range to the new range and clamps it'''
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
    '''    Just like fit() but assumes value is already in the range 0 to 1.'''
    if (val < 0) : return minVal
    if (val > 1): return maxVal
    return lerp(minVal, maxVal, val)


def clamp(val, minVal, maxVal ):
    '''This function clamps the input data between the minimum and maximum values'''
    #return min if val < min else max if val > max else val
    if val<minVal:
        val = minVal
    elif val>maxVal:
        val = maxVal
    return val

def smoothstep(edge0, edge1, x):
    '''Smoothstep is an interpolation function where we assume that the left edge is 0, the right edge is 1, and 0 ≤ x ≤ 1 (https://en.wikipedia.org/wiki/Smoothstep)'''
    x = clamp((x - edge0)/(edge1 - edge0), 0.0, 1.0)
    return x*x*(3 - 2*x)

def smooth(min, max, val):
    '''Outputs a smoothed value between 0 and 1 as value goes from minimum to maximum.'''
   if (val <= min) : return 0
   if (val >= max) : return 1
   t = max - min
   if equalZero(t,1e-18) : return 0.5
   t = (val - min) / t
   return t*t*(3.0 - 2.0*t)

def smooth01(min, max, val, roll):
    '''Ease-in ease-out curve (with rolloff)'''
    if (roll > 0):
        f = smooth(min, max, val)
        return 1-(pow(1-f,1/roll)) if roll < 1 else pow(f,roll)
    return 1



