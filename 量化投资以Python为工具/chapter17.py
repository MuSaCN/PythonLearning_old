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
Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码"
Path2="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\习题解答"

#chap17 regression
import pandas as pd
Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码"
TRD_Index=pd.read_table(Path+'/017/TRD_Index.txt',sep='\t')
SHindex=TRD_Index[TRD_Index.Indexcd==1]
SZindex=TRD_Index[TRD_Index.Indexcd==399106]
SHRet=SHindex.Retindex
SZRet=SZindex.Retindex
SZRet.index=SHRet.index

import statsmodels.api as sm
model=sm.OLS(SHRet,sm.add_constant(SZRet)).fit()

myfigpro.ScatterAndRegression(SZRet,SHRet,None,0,True)

import statsmodels.formula.api as smf
news=pd.concat([SHRet,SZRet],axis=1)
news.columns=["SH","SZ"]
a=myDA.ols("SH~SZ",data=news,summary=False)
myDA.ols_FittedvaluesResidScatter(a)

a.fittedvalues #拟合值
a.resid        #残差
a.summary()    #摘要


print(model.summary())
a.fittedvalues[:5]


import matplotlib.pyplot as plt

myfig.PlotScatter(model.fittedvalues,model.resid,size=1)
myfigpro.ScatterAndRegression(model.fittedvalues,model.resid)


import scipy.stats as stats
myDA.ols_qqplot(model)
sm.qqplot(model.resid_pearson,stats.norm,line='45')
plt.show()

pd.Series(model.resid).hist(bins=100)
plt.show()


plt.scatter(model.fittedvalues,model.resid_pearson**0.5)
plt.xlabel('拟合值')
plt.ylabel('标准化残差的平方根')
plt.show()


Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码"
penn=pd.read_excel(Path+'/017/Penn World Table.xlsx',2)
PEEN=myfile.read_pd(Path+'/017/Penn World Table.xlsx',sheet_name=2)

penn.head(3)
import numpy as np
model=sm.OLS(np.log(penn.rgdpe),sm.add_constant(penn.iloc[:,-6:])).fit()
print(model.summary())
PEEN.columns
myDA.ols("np.log(rgdpe) ~ pl_c+ pl_i+ pl_g+ pl_x+ pl_m+ pl_k",PEEN,True)


penn.iloc[:,-6:].corr()

model=sm.OLS(np.log(penn.rgdpe),\
             sm.add_constant(penn.iloc[:,-5:-1])).fit()
print(model.summary())



















