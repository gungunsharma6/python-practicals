# to remove all the leading and trailing white spaces fromn each element of array
import numpy as np
a=['    python',' c++   ','c  ',' java','gla ']
a=np.array(a)
print('original array: ',a)
strip_array=np.char.strip(a)
print('new array: ',strip_array)