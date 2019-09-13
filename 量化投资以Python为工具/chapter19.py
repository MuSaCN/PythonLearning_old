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
Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码\\019"
Path2="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\习题解答"

stock=myfile.read_pd(Path+'/stock.txt',sep="\t",index="Trddt",parse_dates=True)
fjgs = stock.ix[stock.Stkcd == 600033, 'Dretwd']
fjgs.name = 'fjgs'
zndl = stock.ix[stock.Stkcd == 600023, 'Dretwd']
zndl.name = 'zndl'
sykj = stock.ix[stock.Stkcd == 600183, 'Dretwd']
sykj.name = 'sykj'
hxyh = stock.ix[stock.Stkcd == 600015, 'Dretwd']
hxyh.name = 'hxyh'
byjc = stock.ix[stock.Stkcd == 600004, 'Dretwd']
byjc.name = 'byjc'
sh_return = pd.concat([byjc, fjgs, hxyh, sykj, zndl], axis=1)
sh_return = sh_return.dropna()
cumreturn = (1 + sh_return).cumprod()


train_set = sh_return['2014']
test_set = sh_return['2015']

P = np.array([[ 1. ,  0. ,  1. ,  1. ,  1. ],
              [ 0.5,  0.5,  0. ,  0. , -1. ]])
Q = np.array([0.003,0.001])

P1 = np.array([[ 1. ,  0. ,  1. ,  1. ,  1. ],
               [ 1,    0,    0. ,  0. , -1. ],
               [ 0,    1,    0. ,  0. , -1. ]])
Q1 = np.array([0.003,0.001,0.001])


myDA.BlackLitterman_OptWeight(sh_return,0.3,P,Q,0.002)

myDA.BlackLitterman_OptWeight(sh_return,0.3,P1,Q1,0.002)






