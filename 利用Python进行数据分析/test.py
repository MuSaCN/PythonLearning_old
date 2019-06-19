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

## Hierarchical Indexing
#%%
data=mypd.Series(np.random.randn(9),index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 3, 1, 2, 2, 3]])
data
#%%
data.index
#%%
data['b']
data['b':'c']
data.loc[['b', 'd']]
#%%
data.loc[:, 2]
#%%
data.unstack()
#%%
data.unstack().stack()
#%%
frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
frame
#%%
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
frame
#%%
frame['Ohio']
#%% md
MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']],
                       names=['state', 'color'])
#%% md
### Reordering and Sorting Levels
#%%
frame.swaplevel('key1', 'key2')
#%%
frame.sort_index(level=1)
frame.swaplevel(0, 1).sort_index(level=0)
#%% md
### Summary Statistics by Level
#%%
frame.sum(level='key2')
frame.sum(level='color', axis=1)
#%%
frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two',
                            'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
frame
#%%
frame2 = frame.set_index(['c', 'd'])
frame2
frame3=frame2.set_index(["a"],drop=True)
frame3.reset_index().reset_index()
#%%
frame.set_index(['c', 'd'], drop=False)
#%%
frame2.reset_index()

