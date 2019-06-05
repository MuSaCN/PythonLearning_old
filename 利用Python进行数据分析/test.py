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

#------------------------------------------
#---K个最邻近点
#mypltpro.KNearest(2,mynp.gen_random("random",-500,500,shape=(100,2)),axesindex=0,OnlyScatter=False)
myplt.__init__()
nwalks=5000
nsteps=1000
draws=mynp.gen_random("randint",0,1,shape=(nwalks,nsteps))
steps=mynp.where(draws>0,1,-1)
walk=steps.cumsum()
myplt.PlotLine2D(0,walk)
walk.min()
walk.max()
(mynp.abs(walk) >=10).argmax()















