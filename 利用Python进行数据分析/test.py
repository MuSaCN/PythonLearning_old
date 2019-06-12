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
a=mypd.DataFrame(mynp.gen_random(0,10,shape=[4,4]),index=["a","a","c","d"],columns=["A","B","C","D"])
b=mypd.Series([i for i in range(5)])
a
b
a.corr()
b.corr(b)

