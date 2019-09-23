# Author:Zhang Yuan
import MyPackage
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import statsmodels.api as sm
from scipy import stats

#------------------------------------------------------------
__mypath__ = MyPackage.MyClass_Path.MyClass_Path("\\量化投资以Python为工具")  #路径类
myfile = MyPackage.MyClass_File.MyClass_File()  #文件操作类
myplt = MyPackage.MyClass_Plot.MyClass_Plot()  #直接绘图类(单个图窗)
myfig = MyPackage.MyClass_Plot.MyClass_Figure()  #对象式绘图类(可多个图窗)
mypltpro = MyPackage.MyClass_PlotPro.MyClass_PlotPro()  #Plot高级图系列
myfigpro = MyPackage.MyClass_PlotPro.MyClass_FigurePro()  #Figure高级图系列
mynp = MyPackage.MyClass_Array.MyClass_NumPy()  #多维数组类(整合Numpy)
mypd = MyPackage.MyClass_Array.MyClass_Pandas()  #矩阵数组类(整合Pandas)
mypdpro = MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
mytime = MyPackage.MyClass_Time.MyClass_Time()  #时间类
myDA = MyPackage.MyClass_DataAnalysis.MyClass_DataAnalysis()  #数据分析类
#MyPackage.MyClass_ToDefault.DefaultMatplotlibBackend()       #恢复默认设置(仅main主界面)
#------------------------------------------------------------
Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码\\024"
Path2="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\习题解答"

from statsmodels.graphics.tsaplots import *
from statsmodels.tsa import stattools
from statsmodels.tsa import arima_model
import math

#读取数据
CPI=pd.read_csv('CPI.csv',index_col='time')
#将数据转换成时间序列格式
CPI.index=pd.to_datetime(CPI.index)
#查看前3行数据
CPI.head(n=3)
#查看后3行数据
CPI.tail(n=3)
CPI.shape

#剔除最后3期数据,构造用于建模的数据子集
CPItrain=CPI[3:]
CPItrain.head(n=3)
#绘制时序图，直观了解数据情况
CPI.sort().plot(title='CPI 2001-2014')

#进行ADF单位根检验，并查看结果；
CPItrain=CPItrain.dropna().CPI

print(ADF(CPItrain,max_lags=10).summary().as_text())
#lag即为上述检验表达式中的m，在这里我们选择检验12阶的自相关系数。
LjungBox=stattools.q_stat(stattools.acf(CPItrain)[1:12],len(CPItrain))
LjungBox[1][-1]

#将画面一分为二
axe1=plt.subplot(121)
axe2=plt.subplot(122)
#在第一个画面中画出序列的自相关系数图
plot1=plot_acf(CPItrain,lags=30,ax=axe1)
#在第二个画面中画出序列的偏自相关系数图
plot2=plot_pacf(CPItrain,lags=30,ax=axe2)

#order表示建立的模型的阶数，c(1,0,1)表示建立的是ARMA(1,1)模型；
#中间的数字0表示使用原始的、未进行过差分（差分次数为0）的数据；
#此处我们无需考虑它
model1=arima_model.ARIMA(CPItrain,order=(1,0,1)).fit()
model1.summary()

#同理，我们建立起其它阶数的模型
model2=arima_model.ARIMA(CPItrain,order=(1,0,2)).fit()
model2.summary()
model3=arima_model.ARIMA(CPItrain,order=(2,0,1)).fit()
model4=arima_model.ARIMA(CPItrain,order=(2,0,2)).fit()
model5=arima_model.ARIMA(CPItrain,order=(3,0,1)).fit()
model6=arima_model.ARIMA(CPItrain,order=(3,0,2)).fit()

model6.conf_int()
#绘制时间序列模拟的诊断图
stdresid=model6.resid/math.sqrt(model6.sigma2)
plt.plot(stdresid)
plot_acf(stdresid,lags=20)
LjungBox=stattools.q_stat(stattools.acf(stdresid)[1:13],len(stdresid))
LjungBox[1][-1]
LjungBox=stattools.q_stat(stattools.acf(stdresid)[1:20],len(stdresid))
LjungBox[1][-1]
plot_acf(stdresid,lags=40)

model6.forecast(3)[0]
CPI.head(3)

#上证指数的平稳时间序列建模

Datang=pd.read_csv('Datang.csv',index_col='time')
Datang.index=pd.to_datetime(Datang.index)
Datang.head()
returns=Datang.datang['2014-01-01':'2016-01-01']
returns.head(n=3)
returns.tail(n=3)
returns.plot()


ADF(returns).summary()


stattools.q_stat(stattools.acf(returns)[1:12],len(returns))[1]

stattools.arma_order_select_ic(returns,max_ma=4)
model=arima_model.ARIMA(returns,order=(1,0,0)).fit()
model.summary()
model.conf_int()
stdresid=model.resid/math.sqrt(model.sigma2)
plt.plot(stdresid)
plot_acf(stdresid,lags=12)
LjungBox=stattools.q_stat(stattools.acf(stdresid)[1:12],len(stdresid))
LjungBox[1]








