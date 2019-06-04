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
diff=x[:,np.newaxis,:]-x[np.newaxis,:,:]
diff=x[:,np.newaxis,:]-x
diff.shape
sq=(diff**2).sum(-1)
sq.diagonal()

nearest=np.argsort(sq,axis=1)
nearest=np.array([[5,4,3,2,1],[7,4,1,8,5]])
np.partition(nearest,2,axis=1)
nearest[a[0],a[1]]
'''
array([[0, 8, 3, 2, 1, 7, 6, 9, 5, 4],
       [1, 6, 2, 0, 8, 9, 3, 4, 5, 7],
       [2, 8, 0, 9, 3, 1, 5, 6, 7, 4],
       [3, 8, 0, 2, 7, 1, 9, 5, 6, 4],
       [4, 6, 1, 9, 2, 0, 8, 5, 3, 7],
       [5, 9, 2, 8, 3, 1, 0, 6, 7, 4],
       [6, 1, 4, 0, 2, 8, 9, 3, 5, 7],
       [7, 3, 0, 8, 2, 1, 9, 6, 5, 4],
       [8, 2, 3, 0, 1, 9, 7, 5, 6, 4],
       [9, 5, 2, 1, 8, 3, 0, 6, 4, 7]], dtype=int64)
'''



