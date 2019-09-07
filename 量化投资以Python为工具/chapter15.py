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
#------------------------------------------------------------
Path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\数据及源代码"
Path2="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\量化投资以python为工具\\习题解答"

SHindex=pd.read_csv(Path+'\\part 2\\015\\TRD_Index.csv')
SHindex.head(3)
Retindex=SHindex.Retindex



Retindex.hist()
plt.show()

mu=Retindex.mean()
sigma=Retindex.std()
import matplotlib.pyplot as plt
plt.hist(Retindex,normed=True)
plt.plot(np.arange(-0.06,0.062,0.002),stats.norm.pdf(np.arange(-0.06,0.062,0.002),mu,sigma))
stats.t.interval(0.95,len(Retindex)-1,mu,stats.sem(Retindex))


myfig.ReSetFigureAxes()
myfig.PlotHistogram(Retindex,density=True,show=False)
myfig.NormPlot(mu,sigma)
myfig.PlotLine(np.arange(-0.06,0.062,0.002),stats.norm.pdf(np.arange(-0.06,0.062,0.002),mu,sigma))

TRD_Index=pd.read_table(Path+'\\part 2\\015\\TRD_Index.txt',sep='\t')
SHindex=TRD_Index[TRD_Index.Indexcd==1]
SHRet=SHindex.Retindex
myDA.ttest_1samp(SHRet,0.0002)
stats.ttest_1samp(SHRet,0.0002)

SZindex=TRD_Index[TRD_Index.Indexcd==399106]
SZRet=SZindex.Retindex
myDA.ttest_2samp(SHRet,SZRet,False)

stats.ttest_ind(SHRet,SZRet)
stats.ttest_rel(SHRet,SZRet)




