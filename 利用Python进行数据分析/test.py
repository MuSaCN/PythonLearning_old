# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析")
myplt=MyPackage.MyClass_Plot.MyClass_Figure()
mypltpro=MyPackage.MyClass_PlotPro.MyClass_PlotPro()
mynp=MyPackage.MyClass_Array.MyClass_NumPy()
mypd=MyPackage.MyClass_Array.MyClass_Pandas()
myfile=MyPackage.MyClass_File.MyClass_File()
#------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\ch06"
pd.options.display.max_rows=10
pd.options.display.max_columns=10
it=pd.read_csv(path+"\\ex6.csv",chunksize=1000)
for i in it:
    print(i)
    break


it=myfile.readfile_iter(path+"\\ex6.csv",chunksize=100)
next(it)



