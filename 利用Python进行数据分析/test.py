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
a=mypd.DataFrame(mynp.gen_random(0,10,shape=[4,4]),index=["b","a","c","d"],columns=["A","B","C","D"])
b=mypd.Series([i for i in range(5)])
a
b

mypd.sort(a,"value",["a","b"],1,False)
a.rank()
b.rank()

a
a.sort_index(axis=0,ascending=False)
a.sort_values(by="A",axis=0,ascending=True)

b
b.sort_index(axis=0,ascending=False)
b.sort_values(axis=0,ascending=False)

AA="B" in a.columns
BB="A" in a.index
AA and (not BB)