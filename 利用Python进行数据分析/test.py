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
x=mynp.gen_random(shape=(10,2))
x
myplt.PlotScatter(0,x[:,0],x[:,1])
x[:,np.newaxis,:]
x[np.newaxis,:,:]














