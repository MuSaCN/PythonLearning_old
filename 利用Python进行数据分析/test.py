# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析")
myplt=MyPackage.MyClass_Plot.MyClass_Figure()
mynp=MyPackage.MyClass_Array.MyClass_NumPy()
#------------------------------------------
a=mynp.ndarray([i for i in range(10)])
b=mynp.gen_appoint(10)
c=mynp.gen_range(0,9,1,shape=(1,3,3))
c.shape, c.ndim, c.dtype,c
b.dtype=np.dtype("i2")
b.astype("int64")
b
c
c.astype("S10")
c
a=mynp.ndarray(["adf","34b","fdfc","DDF","EEF","GEF"])
a.astype("U1")









