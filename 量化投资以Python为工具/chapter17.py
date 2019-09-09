# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import statsmodels as sm
from scipy import stats
import MyPackage

__mypath__ = MyPackage.MyClass_Path.MyClass_Path("\\量化投资以Python为工具")  #路径类
myfile = MyPackage.MyClass_File.MyClass_File()            #文件操作类
myplt = MyPackage.MyClass_Plot.MyClass_Plot()             #直接绘图类(单个图窗)
myfig = MyPackage.MyClass_Plot.MyClass_Figure()           #对象式绘图类(可多个图窗)
mypltpro = MyPackage.MyClass_PlotPro.MyClass_PlotPro()    #Plot高级图系列
myfigpro = MyPackage.MyClass_PlotPro.MyClass_FigurePro()  #Figure高级图系列
mynp = MyPackage.MyClass_Array.MyClass_NumPy()            #多维数组类(整合Numpy)
mypd = MyPackage.MyClass_Array.MyClass_Pandas()           #矩阵数组类(整合Pandas)
mypdpro = MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
mytime = MyPackage.MyClass_Time.MyClass_Time()            #时间类
myDA = MyPackage.MyClass_DataAnalysis.MyClass_DataAnalysis()  #数据分析类
#------------------------------------------------------------

#chap17 regression
import pandas as pd
TRD_Index=pd.read_table('017/TRD_Index.txt',sep='\t')
SHindex=TRD_Index[TRD_Index.Indexcd==1]
SZindex=TRD_Index[TRD_Index.Indexcd==399106]
SHRet=SHindex.Retindex
SZRet=SZindex.Retindex
SZRet.index=SHRet.index

import statsmodels.api as sm
model=sm.OLS(SHRet,sm.add_constant(SZRet)).fit()
print(model.summary())
model.fittedvalues[:5]

import matplotlib.pyplot as plt
plt.scatter(model.fittedvalues,model.resid)
plt.xlabel('拟合值')
plt.ylabel('残差')

import scipy.stats as stats
sm.qqplot(model.resid_pearson,\
              stats.norm,line='45')

plt.scatter(model.fittedvalues,\
             model.resid_pearson**0.5)
plt.xlabel('拟合值')
plt.ylabel('标准化残差的平方根')

penn=pd.read_excel('017/Penn World Table.xlsx',2)
penn.head(3)
import numpy as np
model=sm.OLS(np.log(penn.rgdpe),
             sm.add_constant(penn.iloc[:,-6:])).fit()
print(model.summary())

penn.iloc[:,-6:].corr()

model=sm.OLS(np.log(penn.rgdpe),\
             sm.add_constant(penn.iloc[:,-5:-1])).fit()
print(model.summary())
