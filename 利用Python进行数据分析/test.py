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

myfigpro.ReSetFigureAxes(1,1)

tips = pd.read_csv(path+'examples\\tips.csv')
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.loc[:, 2:5]
party_pcts = party_counts.div(party_counts.sum(1), axis=0)
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

myfigpro.ScatterMatrix(tips,reg=True,density=True,show=False)
myfigpro.PlotSave("ScatterMatrix.jpg")


sns.pairplot(tips,hue="time",diag_kind="kde")
sns.pairplot(tips,hue="time",diag_kind="kde",kind="reg")
sns.pairplot(tips, kind="reg",ax=myfig.AxesList[0])
plt.show()


macro = pd.read_csv(path+'examples\\macrodata.csv')
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
trans_data[-5:]

myfigpro.ScatterAndRegression(trans_data['m1'],trans_data['unemp'])


#%%
sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})
sns.pairplot(trans_data,hue="cpi")
plt.show()



#%% md
### Facet Grids and Categorical Data
#%%
sns.factorplot(x='day', y='tip_pct', hue='time', col='smoker',
               kind='bar', data=tips[tips.tip_pct < 1])
#%%
sns.factorplot(x='day', y='tip_pct', row='time',
               col='smoker',
               kind='bar', data=tips[tips.tip_pct < 1])
#%%
sns.factorplot(x='tip_pct', y='day', kind='box',
               data=tips[tips.tip_pct < 0.5])
#%% md
## Other Python Visualization Tools
#%%
pd.options.display.max_rows = PREVIOUS_MAX_ROWS
#%% md
## Conclusion






































