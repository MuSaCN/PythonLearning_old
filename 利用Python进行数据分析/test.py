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


frame = pd.DataFrame({'data1': np.random.randn(1000),'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4,labels=False)
quartiles[:10]
#%%
def get_stats(group):
    return {'min': group.min(), 'max': group.max(),
            'count': group.count(), 'mean': group.mean()}
grouped = frame.data2.groupby(quartiles)
mypd.GroupByPrint(grouped)
grouped.head()
grouped.apply(get_stats).unstack()
#%%
# Return quantile numbers
grouping = pd.qcut(frame.data1, 10, labels=False)
grouping = pd.qcut(frame.data1, 10, labels=None)
grouping[0]
grouped = frame.data2.groupby(grouping)
grouped.apply(get_stats).unstack()

s = pd.Series(np.random.randn(6))
s[::2] = np.nan
s
s.fillna(s.mean())
#%%
states = ['Ohio', 'New York', 'Vermont', 'Florida','Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
data
#%%
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
data
data.groupby(group_key).mean()
mypd.GroupByPrint(data.groupby(group_key))
a=data.groupby(group_key)
a.apply(lambda x:x.name)


tips = pd.read_csv(path+'examples\\tips.csv')
# Add tip percentage of total bill
tips['tip_pct'] = tips['tip'] / tips['total_bill']
tips[:6]
grouped = tips.groupby(['day', 'smoker'])
grouped.apply(lambda x:x.name)




#%%
fill_mean = lambda g: g.fillna(g.mean())
data.groupby(group_key).apply(fill_mean)
#%%
fill_values = {'East': 0.5, 'West': -1}
fill_func = lambda g: g.fillna(fill_values[g.name])
data.groupby(group_key).apply(fill_func)



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
deck.groupby(get_suit).head()
#%%
deck.groupby(get_suit, group_keys=False).apply(draw, n=2)





















