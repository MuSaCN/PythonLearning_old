# Author:Zhang Yuan

from MyPackage import MyClass_Path
from MyPackage import MyClass_File

__mypath__ = MyClass_Path.MyClass_Path()  #路径类
myfile = MyClass_File.MyClass_File()  #文件操作类

MyPackage_PathList = __mypath__.GetMyPackagePath()
myfile.ZipDir(MyPackage_PathList[0], zipPath="Desktop" , zipName=None, autoName=True)





