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
a=mynp.gen_range(0,20,1,shape=(2,10))
b=mynp.gen_range(0,mynp.pi,6,"linspace")
aa=mynp.ndarray([mynp.e,1])
c=mynp.log(aa,False)
c












