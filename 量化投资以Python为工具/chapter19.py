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


#import ffn
from scipy import linalg


class MeanVariance:
    def __init__(self, returns):
        self.returns = returns

    def minVar(self, goalRet):
        covs = np.array(self.returns.cov())
        means = np.array(self.returns.mean())
        L1 = np.append(np.append(covs.swapaxes(0, 1), [means], 0),
                       [np.ones(len(means))], 0).swapaxes(0, 1)
        L2 = list(np.ones(len(means)))
        L2.extend([0, 0])
        L3 = list(means)
        L3.extend([0, 0])
        L4 = np.array([L2, L3])
        L = np.append(L1, L4, 0)
        results = linalg.solve(L, np.append(np.zeros(len(means)), [1, goalRet], 0))
        return (np.array([list(self.returns.columns), results[:-2]]))

    def frontierCurve(self):
        goals = [x / 500000 for x in range(-100, 4000)]
        variances = list(map(lambda x: self.calVar(self.minVar(x)[1, :].astype(np.float)), goals))
        plt.plot(variances, goals)

    def meanRet(self, fracs):
        meanRisky = myDA.p_to_returns(self.returns).mean()
        assert len(meanRisky) == len(fracs), 'Length of fractions must be equal to number of assets'
        return (np.sum(np.multiply(meanRisky, np.array(fracs))))

    def calVar(self, fracs):
        return (np.dot(np.dot(fracs, self.returns.cov()), fracs))


minVar = MeanVariance(sh_return)
minVar.frontierCurve()
plt.show()




train_set = sh_return['2014']
test_set = sh_return['2015']
varMinimizer = MeanVariance(train_set)
goal_return = 0.003
portfolio_weight = varMinimizer.minVar(goal_return)
portfolio_weight
test_return = np.dot(test_set,
                     np.array([portfolio_weight[1, :].astype(np.float)]).swapaxes(0, 1))
test_return = pd.DataFrame(test_return, index=test_set.index)
test_cum_return = (1 + test_return).cumprod()

sim_weight = np.random.uniform(0, 1, (100, 5))
sim_weight = np.apply_along_axis(lambda x: x / sum(x), 1, sim_weight)
sim_return = np.dot(test_set, sim_weight.swapaxes(0, 1))
sim_return = pd.DataFrame(sim_return, index=test_cum_return.index)
sim_cum_return = (1 + sim_return).cumprod()

plt.plot(sim_cum_return.index, sim_cum_return, color='green')
plt.plot(test_cum_return.index, test_cum_return)


def blacklitterman(returns, tau, P, Q):
    mu = returns.mean()
    sigma = returns.cov()
    pi1 = mu
    ts = tau * sigma
    Omega = np.dot(np.dot(P, ts), P.T) * np.eye(Q.shape[0])
    middle = linalg.inv(np.dot(np.dot(P, ts), P.T) + Omega)
    er = np.expand_dims(pi1, axis=0).T + np.dot(np.dot(np.dot(ts, P.T), middle),
                                                (Q - np.expand_dims(np.dot(P, pi1.T), axis=1)))
    posteriorSigma = sigma + ts - np.dot(ts.dot(P.T).dot(middle).dot(P), ts)
    return [er, posteriorSigma]


pick1 = np.array([1, 0, 1, 1, 1])
q1 = np.array([0.003 * 4])
pick2 = np.array([0.5, 0.5, 0, 0, -1])
q2 = np.array([0.001])
P = np.array([pick1, pick2])
Q = np.array([q1, q2])
P
Q

res = blacklitterman(sh_return, 0.1, P, Q)
p_mean = pd.DataFrame(res[0], index=sh_return.columns, columns=['posterior_mean'])
p_mean
p_cov = res[1]
p_cov


def blminVar(blres, goalRet):
    covs = np.array(blres[1])
    means = np.array(blres[0])
    L1 = np.append(np.append((covs.swapaxes(0, 1)), [means.flatten()], 0),
                   [np.ones(len(means))], 0).swapaxes(0, 1)
    L2 = list(np.ones(len(means)))
    L2.extend([0, 0])
    L3 = list(means)
    L3.extend([0, 0])
    L4 = np.array([L2, L3])
    L = np.append(L1, L4, 0)
    results = linalg.solve(L, np.append(np.zeros(len(means)), [1, goalRet], 0))
    return (pd.DataFrame(results[:-2],
                         index=blres[1].columns, columns=['p_weight']))


blminVar(res, 0.75 / 252)



