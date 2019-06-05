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
#---对外接口：k值，axesindex，N*2结构[[x1,y1],[x2,y2]...]的数据
k=3
axesindex=0
#---接受N*2的数据结构[[x1,y1],[x2,y2]...]
x=mynp.gen_random(shape=(10,2))
myplt.PlotScatter(0,x[:,0],x[:,1])

#---批量生成距离差，每个点都匹配
diff=x[:,np.newaxis,:]-x #注意减号前后不同，结果意义不同
#---SquareDistance为平方距离
SquareDistance=(diff**2).sum(axis=2)
#---获得距离，数据意义：[[p0-p0,p0-p1...],[p1-p0,p1-p1...],...]
Distance=SquareDistance**0.5

#---获得排序序号
nearest=np.argsort(Distance,axis=1)

#---获得k个最邻近的序号(k个最小值分割到前面)
nearest_partition=np.argpartition(Distance,k+1,axis=1)
#---清理指定的axes
myplt.ClearAxes(axesindex)
#---画图
for i in range(x.shape[0]):
    for j in nearest_partition[i,:k+1]:
        #画从x[i]到x[j]的线段(x[i]为点坐标)
        myplt.PlotLine2Dot(axesindex,x[i],x[j],"",cla=False,show=False)
myplt.FigureShow()







