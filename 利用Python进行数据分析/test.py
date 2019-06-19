# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析")
myplt=MyPackage.MyClass_Plot.MyClass_Figure()
mypltpro=MyPackage.MyClass_PlotPro.MyClass_PlotPro()
mynp=MyPackage.MyClass_Array.MyClass_NumPy()
mypd=MyPackage.MyClass_Array.MyClass_Pandas()
myfile=MyPackage.MyClass_File.MyClass_File()
#------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\ch02"



#%%
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])
df1 = pd.Series([0, 1], index=['a', 'b'])
df2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
df3 = pd.Series([5, 6], index=['f', 'g'])


#%%
result = mypd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
result
result.unstack()
#%%
mypd.concat([df1, df2, df3], axis=1, keys=['one', 'two', 'three'])
#%%
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])
df1
df2
mypd.concat([df1, df2], axis=1, keys=['level1', 'level2'])
#%%
mypd.concat({'level1': df1, 'level2': df2}, axis=1)
#%%
mypd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])
#%%
df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])
df1
df2
#%%
mypd.concat([df1, df2], axis=1,ignore_index=True,keys=["A","B"],names=["aa","bb"])


