'''
Personnal Math 3d Module
'''

def clamp(val, mini, maxi):
    if val<mini:
        val = mini
    elif val > maxi:
        val = maxi
    return val


    
if __name__ == '__main__':
  print clamp(45,0,6)
