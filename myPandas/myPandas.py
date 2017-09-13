import pandas as pd
import numpy as np
import matplotlib as plt

s = pd.Series([1,3,5,np.nan,6,8])


# s:
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

# print('s:',s)

datas = pd.date_range('20170912',periods=6)


# datas:
#     DatetimeIndex(['2017-09-12', '2017-09-13', '2017-09-14', '2017-09-15',
#                '2017-09-16', '2017-09-17'],
#               dtype='datetime64[ns]', freq='D')
# print('datas:',datas)

df = pd.DataFrame(np.random.rand(6,4), index=datas, columns=list('ABCD'))

# df:
#             A         B         C         D
# 2017-09-12  0.898601  0.202429  0.077874  0.414484
# 2017-09-13  0.371581  0.294308  0.875121  0.702701
# 2017-09-14  0.619098  0.664859  0.983480  0.117615
# 2017-09-15  0.534426  0.231214  0.703543  0.460263
# 2017-09-16  0.106504  0.811795  0.325020  0.252612
# 2017-09-17  0.997008  0.410798  0.942508  0.185737

# print('df:',df)