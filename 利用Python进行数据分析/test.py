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
mytime=MyPackage.MyClass_Time.MyClass_Time()            #时间类
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"

#%% md
## Moving Window Functions
#%%
close_px_all = pd.read_csv('examples/stock_px_2.csv',
                           parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
#%%
close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot()
#%%
plt.figure()
#%%
appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
appl_std250[5:12]
appl_std250.plot()
#%%
expanding_mean = appl_std250.expanding().mean()
#%%
plt.figure()
#%%
close_px.rolling(60).mean().plot(logy=True)
#%%
close_px.rolling('20D').mean()
#%% md
### Exponentially Weighted Functions
#%%
plt.figure()
#%%
aapl_px = close_px.AAPL['2006':'2007']
ma60 = aapl_px.rolling(30, min_periods=20).mean()
ewma60 = aapl_px.ewm(span=30).mean()
ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-', label='EW MA')
plt.legend()
#%% md
### Binary Moving Window Functions
#%%
plt.figure()
#%%
spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()
#%%
corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
#%%
plt.figure()
#%%
corr = returns.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
#%% md
### User-Defined Moving Window Functions
#%%
plt.figure()
#%%
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
#%%
pd.options.display.max_rows = PREVIOUS_MAX_ROWS
#%% md
## Conclusion




