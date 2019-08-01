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
mypdpro=MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
mytime=MyPackage.MyClass_Time.MyClass_Time()            #时间类
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\examples\\"
path1="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\Python数据科学手册\\notebooks\\data\\"
myfig.SetAxes_3D2D()
myfig.ReSetFigureAxes()
# myfig.AxesList[0].
# myfig.fig.
myfig.FigureShow()
plt.show()


a=pd.DataFrame(np.random.random((10,5)))
a
a.drop(labels=None,axis=0)

b=np.random.random(10)
b.ptp()
a=pd.Series([3.43,3.45,	3.43,	3.48	,3.52	,3.50	,3.39,3.48,	3.41,	3.38	,3.49	,3.45,	3.51,	3.50])
a
np.var(a)*14/13
a.var()
np.std(a)
a.std()/(14**0.5)

pd.DatetimeIndex(a[0])

a.sem()













