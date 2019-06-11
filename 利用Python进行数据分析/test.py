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
#------------------------------------------
d=mypd.Series([1,5,9,7],index=["a","b","c","d"])
mypd.reindex(d,index=[0,1,2,3,4,5],columns=None)
mypd.reindex(d,index=[0,1,2,3,4,5],columns=None,fillnan="adsf")

a=mypd.DataFrame(np.arange(16).reshape(4,4),index=["a","b","c","d"],columns=["A","B","C","D"])
mypd.reindex(a,index=[0,1,2,3,4,5],columns=[0,1,2,3,4,5,6])
mypd.reindex(a,index=[0,1,2,3,4,5],columns=[0,1,2,3,4,5,6],fillnan=3.14)
b=a+1
mypd.reindex(b,index=["a","b","c","d","e"],fillnan=3.14)
a
d
a.add(d,axis=None)













