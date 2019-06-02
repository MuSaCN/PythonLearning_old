# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
from MyPackage.MyClass_Path import MyClass_Path
__Class_Path__=MyClass_Path("\\利用Python进行数据分析")
from MyPackage.MyClass_Plot import MyClass_Figure
Class_Figure=MyClass_Figure()
#------------------------------------------
m=np.ones([3,3])
a=np.array([0,1,1])
b=np.array([0,1,0])
a | b
b=np.array([[1]])
np.add(a,m)
m+b
c=np.array([[1]])
m+c
d=np.array([[[1],2]])
m+d
x=np.linspace(0,5,50)
y=np.linspace(0,5,50)[:,np.newaxis]
z=np.sin(x)**10+np.cos(10+y*x)*np.cos(x)
z
plt.imshow(z)
plt.show()






