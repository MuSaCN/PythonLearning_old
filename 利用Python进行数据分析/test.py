# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析") #路径类
myfile=MyPackage.MyClass_File.MyClass_File()            #文件操作类
myplt=MyPackage.MyClass_Plot.MyClass_Plot()             #直接绘图类(单个图窗)
myfig=MyPackage.MyClass_Plot.MyClass_Figure()           #对象式绘图类(可多个图窗)
myfigpro=MyPackage.MyClass_PlotPro.MyClass_FigurePro()  #高级对象式绘图类
mynp=MyPackage.MyClass_Array.MyClass_NumPy()            #多维数组类(整合Numpy)
mypd=MyPackage.MyClass_Array.MyClass_Pandas()           #矩阵数组类(整合Pandas)
mypdpro=MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"

tips = pd.read_csv(path+'examples\\tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

## Pivot Tables and Cross-Tabulation
#%%
tips.pivot_table(index=['day', 'smoker'])
#%%
tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'],
                 columns='smoker')
#%%
tips.pivot_table(['tip_pct', 'size'], index=['time', 'day'],
                 columns='smoker', margins=True)
#%%
tips.pivot_table('tip_pct', index=['time', 'smoker'], columns='day',
                 aggfunc=len, margins=True)
#%%
tips.pivot_table('tip_pct', index=['time', 'size', 'smoker'],
                 columns='day', aggfunc='mean', fill_value=0)
#%% md
### Cross-Tabulations: Crosstab
#%%
from io import StringIO
data = """\
Sample  Nationality  Handedness
1   USA  Right-handed
2   Japan    Left-handed
3   USA  Right-handed
4   Japan    Right-handed
5   Japan    Left-handed
6   Japan    Right-handed
7   USA  Right-handed
8   USA  Left-handed
9   Japan    Right-handed
10  USA  Right-handed"""
data = pd.read_table(StringIO(data), sep='\s+')
#%%
data
#%%
pd.crosstab(data.Nationality, data.Handedness, margins=True)
#%%
pd.crosstab([tips.time, tips.day], tips.smoker, margins=True)
#%%
pd.options.display.max_rows = PREVIOUS_MAX_ROWS
#%% md
## Conclusion














