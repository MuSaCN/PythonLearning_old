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

a=myfile.read_lib(path+"\\ex7.csv",sep=",",isheader=False,toDataFrame=True,quotechar='"')
a

content=[]
content.append(["asdf,fdsa,fdas",123,"asdf,fdsa,fdas"])
content.append(["“我爱'你'中国”",432,"“你爱'我'中国吗"])
myfile.write_lib(content,"out.csv","w",";",'.')
myfile.read_lib("out.csv",";",False,False,".")






