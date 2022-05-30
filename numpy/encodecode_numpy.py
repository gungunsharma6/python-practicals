#to encode all elements of an array and then decode them
import numpy as np
a=['python','c++','c','java','gla']
a=np.array(a)
print('original array: ',a)
encode_array=np.char.encode(a,'cp500')
print('new array: ',encode_array)
decode_array=np.char.decode(encode_array,'cp500')
print('array after decoding : ',decode_array)