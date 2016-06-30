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
   smooth(min, max, val)            - Ease-in ease-out curve
   smooth(min, max, a, roll)      - Ease-in ease-out curve (with rolloff)
   lerp(v1, v2, t)                - Linear interpolation
   fit(val, omin,omax, nmin,nmax) - Map val in (oldmin,oldmax) to (newmin,newmax)

SOURCES:
functions definitions
   http://www.andynicholas.com/?p=1344
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
   
smooth
   https://en.wikipedia.org/wiki/Smoothstep
   http://www.sidefx.com/docs/hdk15.0/_s_y_s___math_8h_source.html
   line 709
'''

def equalZero(a, tol=0.00001):
   '''
   Is a equal to zero
   '''
   return a >= -tol and a <= tol
    
def lerp(v1,v2, t):
   '''
   Linear interpolation
   '''
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


   
def smooth(min, max, val):
   '''
   Outputs a smoothed value between 0 and 1 as value goes from minimum to maximum.
   
   Other method (wikipedia):
   x = clamp((x - min)/(max - min), 0.0, 1.0);
   return x*x*(3 - 2*x)
   '''
   
   if (val <= min) : return 0
   if (val >= max) : return 1
   t = max - min
   if t < 1e-8 : return 0.5
   t = (val - min) / t
   return t*t*(3.0 - 2.0*t)    

def smooth01(min, max, val, roll):
   if (roll > 0):
      f = smooth(min, max, val)
      return 1-(pow(1-f,1/roll)) if roll < 1 else pow(f,roll)
   return 1

def barycentric(v1, v2, v3, u, v)
   '''
   Barycentric coordinates do interpolation over the triangle specified by the
   three vertices (v1, v2, v3): 
   
                     (u=0,v=1)              
                         v2                 
                         / \                  
                        /   \                
                       /     \               
            (u=0,v=0) v0------v1 (u=1,v=0)
   '''
   return v1*(1-u-v) + v2*u + v3*v    
    
if __name__ == '__main__':
  print clamp(45,0,6)
  print fit(30 , 0 , 90 , 0 , 1)
