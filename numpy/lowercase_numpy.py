#to lowercase all elements of the given array
import numpy as np
a=['PYTHON','C++','C','JAVA','GlA']
a=np.array(a)
print('original array: ',a)
lower_case=np.char.lower(a)
print('new array : ',lower_case)