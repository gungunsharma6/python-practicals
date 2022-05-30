# to remove all the leading white spaces fromn each element of array
import numpy as np
a=['    python',' c++   ','c  ',' java','gla ']
a=np.array(a)
print('original array: ',a)
lstrip_array=np.char.lstrip(a)
print('new array: ',lstrip_array)