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
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\ch06"

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
Age=pd.Series(ages)
#%%
bins = [18, 25, 35, 60, 100]
qbins=[0, 0.1, 0.5, 0.9, 1.]
a=mypd.cut(ages,4,q=False,right=False,labels=["A","B","C","D"],precision=3)
b=mypd.cut(ages,4,q=True,right=False,precision=3)
a
b
pd.value_counts(a) #-->每个箱元素数量计算
pd.value_counts(b)

a.codes #所属类别
a.categories #类别数组
b.codes
b.categories


cats = pd.cut(ages, bins)
pd.cut(Age, bins)
cats
#%%
cats.labels
#%%
cats.levels
#%%
pd.value_counts(cats)
#%%
pd.cut(ages, [18, 26, 36, 61, 100], right=False)
#%%
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)
#%%
data = np.random.rand(20)
pd.cut(data, 4, precision=2)
#%%
data = np.random.randn(1000) # Normally distributed
cats = pd.qcut(data, 4) # Cut into quartiles
cats
#%%
pd.value_counts(cats)
#%%
pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])

