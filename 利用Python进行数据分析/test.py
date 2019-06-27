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
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"

tips = pd.read_csv(path+'examples\\tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

frame = pd.DataFrame({'data1': np.random.randn(20),'data2': np.random.randn(20)})
mypd.filterAbnormal(frame,lower=0,upper=1,AnyOrAll="any",limited=False)
mypd.get_dummies(frame["data1"])

### Quantile and Bucket Analysis
#%%
frame = pd.DataFrame({'data1': np.random.randn(1000),
                      'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)
quartiles[:10]
#%%
def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}
grouped = frame.data2.groupby(quartiles)
grouped.apply(get_stats).unstack()
#%%
# Return quantile numbers
grouping = pd.qcut(frame.data1, 10, labels=False)
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()
#%% md
### Example: Filling Missing Values with Group-Specific       Values
#%%
s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s
s.fillna(s.mean())
#%%
states = ['Ohio', 'New York', 'Vermont', 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data
#%%
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
data
data.groupby(group_key).mean()
#%%
fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)
#%%
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)
#%% md
### Example: Random Sampling and Permutation
#%%
# Hearts, Spades, Clubs, Diamonds
suits = ['H', 'S', 'C', 'D']
card_val = (list(range(1, 11)) + [10] * 3) * 4
base_names = ['A'] + list(range(2, 11)) + ['J', 'K', 'Q']
cards = []
for suit in ['H', 'S', 'C', 'D']:
    cards.extend(str(num) + suit for num in base_names)

deck = pd.Series(card_val, index=cards)
#%%
deck[:13]
#%%
def draw(deck, n=5):
    return deck.sample(n)
draw(deck)
#%%
get_suit = lambda card: card[-1] # last letter is suit
deck.groupby(get_suit).apply(draw, n=2)
#%%
deck.groupby(get_suit, group_keys=False).apply(draw, n=2)
#%% md
### Example: Group Weighted Average and Correlation
#%%
df = pd.DataFrame({'category': ['a', 'a', 'a', 'a',
                                'b', 'b', 'b', 'b'],
                   'data': np.random.randn(8),
                   'weights': np.random.rand(8)})
df
#%%
grouped = df.groupby('category')
get_wavg = lambda g: np.average(g['data'], weights=g['weights'])
grouped.apply(get_wavg)
#%%
close_px = pd.read_csv('examples/stock_px_2.csv', parse_dates=True,
                       index_col=0)
close_px.info()
close_px[-4:]
#%%
spx_corr = lambda x: x.corrwith(x['SPX'])
#%%
rets = close_px.pct_change().dropna()
#%%
get_year = lambda x: x.year
by_year = rets.groupby(get_year)
by_year.apply(spx_corr)
#%%
by_year.apply(lambda g: g['AAPL'].corr(g['MSFT']))
#%% md
### Example: Group-Wise Linear Regression
#%%
import statsmodels.api as sm
def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params
#%%
by_year.apply(regress, 'AAPL', ['SPX'])
#%% md
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














