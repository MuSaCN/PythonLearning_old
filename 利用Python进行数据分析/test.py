# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析")
myplt=MyPackage.MyClass_Plot.MyClass_Figure()
mynp=MyPackage.MyClass_Array.MyClass_NumPy()
#------------------------------------------
a=mynp.gen_range(-5,5,0.01)
b=mynp.gen_range(-5,5,0.01)
a,b
x,y= mynp.meshgrid(a,b)
print(x,y)
a=mynp.gen_random(shape=(5,3))
a.sum(axis=1)
a.all(0)
mynp.where(a>0.5)
np.where(a>0.5)
a=np.random.randn(10)
len(a)
a.sort()
