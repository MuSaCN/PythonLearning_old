# Author:Zhang Yuan
import MyPackage


__mypath__ = MyPackage.MyClass_Path.MyClass_Path()  #路径类
myfile = MyPackage.MyClass_File.MyClass_File()  #文件操作类

MyPackage_PathList = __mypath__.GetMyPackagePath()

# ---备份到桌面
myfile.ZipDir(MyPackage_PathList[0], zipPath="Desktop" , zipName=None, autoName=True)

# ---备份到OneDrive的Work-Python备份文件夹
ZipPath = __mypath__.GetOneDrivePath() + "\\Work-Python备份"
myfile.ZipDir(MyPackage_PathList[0], zipPath=ZipPath , zipName=None, autoName=True)



