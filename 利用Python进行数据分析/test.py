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
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"


#%%
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df
#%%
melted = pd.melt(df, ['key'])
melted1=mypd.PivotMelt(df,"melt",id_vars= ['key'],value_vars=None)
mypd.PivotMelt(melted1,"pivot","key","variable","value")
melted.pivot('key', 'variable', 'value')
melted
#%%
reshaped = melted.pivot('key', 'variable', 'value')
reshaped
#%%
reshaped.reset_index()
#%%
pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])
#%%
pd.melt(df, value_vars=['A', 'B', 'C'])
pd.melt(df, value_vars=['key', 'A', 'B'])
#%% md















































