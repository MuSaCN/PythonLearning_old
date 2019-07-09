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


### Group Transforms and "Unwrapped" GroupBys
#%%
df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
                   'value': np.arange(12.)})
df
#%%
g = df.groupby('key').value
g.mean()
#%%
g.transform(lambda x: x.mean())
#%%
g.transform('mean')
#%%
g.transform(lambda x: x * 2)
#%%
g.transform(lambda x: x.rank(ascending=False))
#%%
def normalize(x):
    return (x - x.mean()) / x.std()
#%%
g.transform(normalize)
g.apply(normalize)
#%%
g.transform('mean')
normalized = (df['value'] - g.transform('mean')) / g.transform('std')
normalized
#%% md
### Grouped Time Resampling
#%%
N = 15
times = pd.date_range('2017-05-20 00:00', freq='1min', periods=N)
df = pd.DataFrame({'time': times,
                   'value': np.arange(N)})
df
#%%
df.set_index('time').resample('5min').count()
#%%
df2 = pd.DataFrame({'time': times.repeat(3),
                    'key': np.tile(['a', 'b', 'c'], N),
                    'value': np.arange(N * 3.)})
df2[:7]
#%%
time_key = pd.TimeGrouper('5min')
#%%
resampled = (df2.set_index('time')
             .groupby(['key', time_key])
             .sum())
resampled
resampled.reset_index()
#%% md
## Techniques for Method Chaining
#%% md
```python
df = load_data()
df2 = df[df['col2'] < 0]
df2['col1_demeaned'] = df2['col1'] - df2['col1'].mean()
result = df2.groupby('key').col1_demeaned.std()
```
#%% md
```python
# Usual non-functional way
df2 = df.copy()
df2['k'] = v

# Functional assign way
df2 = df.assign(k=v)
```
#%% md
```python
result = (df2.assign(col1_demeaned=df2.col1 - df2.col2.mean())
          .groupby('key')
          .col1_demeaned.std())
```
#%% md
```python
df = load_data()
df2 = df[df['col2'] < 0]
```
#%% md
```python
df = (load_data()
      [lambda x: x['col2'] < 0])
```
#%% md
```python
result = (load_data()
          [lambda x: x.col2 < 0]
          .assign(col1_demeaned=lambda x: x.col1 - x.col1.mean())
          .groupby('key')
          .col1_demeaned.std())
```
#%% md
### The pipe Method
#%% md
```python
a = f(df, arg1=v1)
b = g(a, v2, arg3=v3)
c = h(b, arg4=v4)
```
#%% md
```python
result = (df.pipe(f, arg1=v1)
          .pipe(g, v2, arg3=v3)
          .pipe(h, arg4=v4))
```
#%% md
g = df.groupby(['key1', 'key2'])
df['col1'] = df['col1'] - g.transform('mean')

#%% md
def group_demean(df, by, cols):
    result = df.copy()
    g = df.groupby(by)
    for c in cols:
        result[c] = df[c] - g[c].transform('mean')
    return result

#%% md
result = (df[df.col1 < 0]
          .pipe(group_demean, ['key1', 'key2'], ['col1']))

#%%
pd.options.display.max_rows = PREVIOUS_MAX_ROWS
#%% md
## Conclusion

