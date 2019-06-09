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

a=mypd.Index([1,2,3,4,5,"a","b","c"])
a
mypd.ChangeIndex(a,"delete","b")

