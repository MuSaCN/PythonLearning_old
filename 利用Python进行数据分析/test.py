# Author:Zhang Yuan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import statsmodels as sm
import MyPackage
__mypath__=MyPackage.MyClass_Path.MyClass_Path("\\利用Python进行数据分析") #路径类
myfile=MyPackage.MyClass_File.MyClass_File()            #文件操作类
myplt=MyPackage.MyClass_Plot.MyClass_Plot()             #直接绘图类(单个图窗)
myfig=MyPackage.MyClass_Plot.MyClass_Figure()           #对象式绘图类(可多个图窗)
myfigpro=MyPackage.MyClass_PlotPro.MyClass_FigurePro()  #高级对象式绘图类
mynp=MyPackage.MyClass_Array.MyClass_NumPy()            #多维数组类(整合Numpy)
mypd=MyPackage.MyClass_Array.MyClass_Pandas()           #矩阵数组类(整合Pandas)
mypdpro=MyPackage.MyClass_ArrayPro.MyClass_PandasPro()  #高级矩阵数组类
mytime=MyPackage.MyClass_Time.MyClass_Time()            #时间类
#---------------------------------------------------------
path="C:\\Users\\i2011\\OneDrive\\Book_Code&Data\\利用Python进行数据分析(第二版)代码\\"


## Date and Time Data Types and Tools
#%%
from datetime import datetime
from datetime import timedelta
from dateutil.parser import parse


#%%
datestrs = ['2011-07-06 12:00:00', '2011-08-06 00:00:00']
pd.to_datetime(datestrs)
mypd.to_datetime(datestrs)


from datetime import datetime
dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),datetime(2011, 1, 7), datetime(2011, 1, 8),datetime(2011, 1, 10), datetime(2011, 1, 12)]
ts = pd.Series(np.random.randn(6), index=dates)
ts
#%%
ts.index
#%%
ts + ts[::2]
#%%
ts.index.dtype
#%%
stamp = ts.index[0]
stamp
#%% md
### Indexing, Selection, Subsetting
#%%
stamp = ts.index[2]
ts[stamp]
#%%
ts['1/10/2011']
ts['20110110']
#%%
pd.date_range(start='1/1/2000',end="2/1/2000", freq="D")
mypd.date_range(start='1/1/2000', periods=1000)

longer_ts = pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000', periods=1000))
longer_ts
longer_ts['2001']
#%%
longer_ts['2001-05']
#%%
ts[datetime(2011, 1, 7):]
#%%
ts=pd.DataFrame(ts)
type(ts)

ts['1/6/2011':'1/11/2011']
#%%
ts
ts.truncate(before='1/9/2011')





#%%
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = pd.DataFrame(np.random.randn(100, 4),index=dates,columns=['Colorado', 'Texas','New York', 'Ohio'])
long_df.loc['5-2001']

### Time Series with Duplicate Indices
#%%
dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000','1/2/2000', '1/3/2000'])
dup_ts = pd.Series(np.arange(5), index=dates)
dup_ts
#%%
dup_ts.index.is_unique
#%%
dup_ts['1/3/2000']  # not duplicated
dup_ts['1/2/2000']  # duplicated
#%%
grouped = dup_ts.groupby(level=0)

mypd.GroupByPrint(grouped)

grouped.mean()
grouped.count()


## Date Ranges, Frequencies, and Shifting
#%%
ts
resampler = ts.resample('D')
#%% md
### Generating Date Ranges
#%%
index = pd.date_range('2012-04-01', '2012-06-01')
index
#%%
pd.date_range(start='2012-04-01', periods=20)
pd.date_range(end='2012-06-01', periods=20)
#%%
pd.date_range('2000-01-01', '2000-12-01', freq="M",normalize=True)
#%%
pd.date_range('2012-05-02 12:56:31', periods=5)
#%%
pd.date_range('2012-05-02 12:56:31', periods=5, normalize=True)
#%% md
### Frequencies and Date Offsets
#%%
from pandas.tseries.offsets import Hour, Minute
hour = Hour()
hour
#%%
four_hours = Hour(4)
four_hours
#%%
pd.date_range('2000-01-01', '2000-01-03 23:59', freq='4h')
#%%
Hour(2) + Minute(30)
#%%
pd.date_range('2000-01-01', periods=10, freq='1H30min')
#%% md
#### Week of month dates
#%%
rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')
list(rng)
#%% md
### Shifting (Leading and Lagging) Data
#%%
ts = pd.Series(np.random.randn(4),index=pd.date_range('1/1/2000', periods=4, freq='M'))
ts
ts.shift(2)
ts.shift(-2)
#%% md
ts / ts.shift(1) - 1
#%%
ts.shift(2, freq='M')
#%%
ts.shift(3, freq='D')
ts.shift(1, freq='90T')
#%% md
#### Shifting dates with offsets
#%%
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()
#%%
now + MonthEnd()
now + MonthEnd(2)
#%%
offset = MonthEnd()
offset.rollforward(now)
offset.rollback(now)
#%%
ts = pd.Series(np.random.randn(20),
               index=pd.date_range('1/15/2000', periods=20, freq='4d'))
ts
ts.groupby(offset.rollforward).mean()
#%%
ts.resample('M').mean()
#%% md
## Time Zone Handling
#%%
import pytz
pytz.common_timezones[-10:]
#%%
mypd.country_timezones("CN")

tz = pytz.timezone('America/New_York')
pytz.timezone('Asia/Shanghai')
tz
#%% md
### Time Zone Localization and Conversion
#%%
rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
#%%
print(ts.index.tz)
#%%
pd.date_range('3/9/2012 9:30', periods=10, freq='D', tz='America/New_York')
#%%
ts
a=mypd.tz_convert(ts,'Asia/Shanghai')
a
mypd.tz_convert(a,'America/New_York')

ts_utc = ts.tz_localize('Asia/Shanghai')
ts_utc
ts_utc.index
ts_utc.index.tz is None
ts.index.tz is None
#%%
ts_utc.tz_convert('America/New_York')
#%%
ts_eastern = ts.tz_localize('America/New_York')
ts_eastern.tz_convert('UTC').tz_convert('Europe/Berlin')
ts_eastern.tz_convert('Europe/Berlin')
#%%
ts.index.tz_localize('Asia/Shanghai')
pytz.country_timezones("NZ")

#%% md
### Operations with Time Zone−Aware Timestamp Objects
#%%
mytime.Timestamp("2011-03-12 04:00",tz='Europe/Moscow')
mypd.Timestamp("2011-03-12 04:00",tz='Europe/Moscow')
mypd.country_timezones()
stamp = pd.Timestamp('2011-03-12 04:00')
stamp_utc = stamp.tz_localize('utc')
stamp_utc.tz_convert('America/New_York')
#%%
stamp_moscow = pd.Timestamp('2011-03-12 04:00', tz='Europe/Moscow')
stamp_moscow
#%%
stamp_moscow.value
stamp_moscow.tz_convert('America/New_York').value
#%%
from pandas.tseries.offsets import Hour
stamp = pd.Timestamp('2012-03-12 01:30', tz='US/Eastern')
stamp
stamp + Hour()
#%%
stamp = pd.Timestamp('2012-11-04 00:30', tz='US/Eastern')
stamp
stamp + 2 * Hour()
#%% md
### Operations Between Different Time Zones
#%%
rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts1 = ts[:7].tz_localize('Europe/London')
ts2 = ts1[2:].tz_convert('Europe/Moscow')
result = ts1 + ts2
result.index
#%% md
## Periods and Period Arithmetic
#%%
p = pd.Period("2007-01",freq=None)
p
pd.date_range("2010-01-01","2020-12-31",freq="A")
#%%
p + 5
p - 2
#%%
pd.Period('2014', freq='A-DEC') - p
#%%
rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
mypd.period_range('2000-01-01', '2000-06-30', freq='M')

rng
#%%
pd.Series(np.random.randn(3), index=index)
#%%
values = ['2001-3', '2002-2', '2003-1']
type(values)
mypd.Period(values,freq="Q")

index = pd.PeriodIndex(values,freq="Q")
index
#%% md
### Period Frequency Conversion
#%%
p = pd.Period('2007', freq='A-DEC')
p
p.asfreq('M', how='start')
p.asfreq('M', how='end')
#%%
p = pd.Period('2007', freq='A-JUN')
p
p.asfreq('M', 'start')
p.asfreq('M', 'end')
#%%
p = pd.Period('Aug-2007', 'M')
p.asfreq('A-JUN')
#%%
rng = pd.period_range('2006', '2009', freq='A-DEC')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.asfreq('M', how='start')
#%%
ts.asfreq('B', how='end')
#%% md
### Quarterly Period Frequencies
#%%
p = pd.Period('2012Q4', freq='Q-JAN')
p
#%%
p.asfreq('D', 'start')
p.asfreq('D', 'end')
#%%
p4pm = (p.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
p4pm
p4pm.to_timestamp()
#%%
rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
ts = pd.Series(np.arange(len(rng)), index=rng)
ts
new_rng = (rng.asfreq('B', 'e') - 1).asfreq('T', 's') + 16 * 60
ts.index = new_rng.to_timestamp()
ts
#%% md
### Converting Timestamps to Periods (and Back)
#%%
rng = pd.date_range('2000-01-01', periods=3, freq='M')
ts = pd.Series(np.random.randn(3), index=rng)
ts
pts = ts.to_period()
pts
#%%
rng = pd.date_range('1/29/2000', periods=6, freq='D')
ts2 = pd.Series(np.random.randn(6), index=rng)
ts2
ts2.to_period('M')
#%%
pts = ts2.to_period()
pts
pts.to_timestamp(how='end')
#%% md
### Creating a PeriodIndex from Arrays
#%%
data = pd.read_csv('examples/macrodata.csv')
data.head(5)
data.year
data.quarter
#%%
index = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                       freq='Q-DEC')
index
data.index = index
data.infl
#%% md
## Resampling and Frequency Conversion
#%%
rng = pd.date_range('2000-01-01', periods=100, freq='D')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ts
ts.resample('M').mean()
ts.resample('M', kind='period').mean()
#%% md
### Downsampling
#%%
rng = pd.date_range('2000-01-01', periods=12, freq='T')
ts = pd.Series(np.arange(12), index=rng)
ts
#%%
ts.resample('5min', closed='right').sum()
#%%
ts.resample('5min', closed='right').sum()
#%%
ts.resample('5min', closed='right', label='right').sum()
#%%
ts.resample('5min', closed='right',
            label='right', loffset='-1s').sum()
#%% md
#### Open-High-Low-Close (OHLC) resampling
#%%
ts.resample('5min').ohlc()
#%% md
### Upsampling and Interpolation
#%%
frame = pd.DataFrame(np.random.randn(2, 4),
                     index=pd.date_range('1/1/2000', periods=2,
                                         freq='W-WED'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame
#%%
df_daily = frame.resample('D').asfreq()
df_daily
#%%
frame.resample('D').ffill()
#%%
frame.resample('D').ffill(limit=2)
#%%
frame.resample('W-THU').ffill()
#%% md
### Resampling with Periods
#%%
frame = pd.DataFrame(np.random.randn(24, 4),
                     index=pd.period_range('1-2000', '12-2001',
                                           freq='M'),
                     columns=['Colorado', 'Texas', 'New York', 'Ohio'])
frame[:5]
annual_frame = frame.resample('A-DEC').mean()
annual_frame
#%%
# Q-DEC: Quarterly, year ending in December
annual_frame.resample('Q-DEC').ffill()
annual_frame.resample('Q-DEC', convention='end').ffill()
#%%
annual_frame.resample('Q-MAR').ffill()
#%% md
## Moving Window Functions
#%%
close_px_all = pd.read_csv('examples/stock_px_2.csv',
                           parse_dates=True, index_col=0)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]
close_px = close_px.resample('B').ffill()
#%%
close_px.AAPL.plot()
close_px.AAPL.rolling(250).mean().plot()
#%%
plt.figure()
#%%
appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
appl_std250[5:12]
appl_std250.plot()
#%%
expanding_mean = appl_std250.expanding().mean()
#%%
plt.figure()
#%%
close_px.rolling(60).mean().plot(logy=True)
#%%
close_px.rolling('20D').mean()
#%% md
### Exponentially Weighted Functions
#%%
plt.figure()
#%%
aapl_px = close_px.AAPL['2006':'2007']
ma60 = aapl_px.rolling(30, min_periods=20).mean()
ewma60 = aapl_px.ewm(span=30).mean()
ma60.plot(style='k--', label='Simple MA')
ewma60.plot(style='k-', label='EW MA')
plt.legend()
#%% md
### Binary Moving Window Functions
#%%
plt.figure()
#%%
spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()
#%%
corr = returns.AAPL.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
#%%
plt.figure()
#%%
corr = returns.rolling(125, min_periods=100).corr(spx_rets)
corr.plot()
#%% md
### User-Defined Moving Window Functions
#%%
plt.figure()
#%%
from scipy.stats import percentileofscore
score_at_2percent = lambda x: percentileofscore(x, 0.02)
result = returns.AAPL.rolling(250).apply(score_at_2percent)
result.plot()
#%%
pd.options.display.max_rows = PREVIOUS_MAX_ROWS
#%% md
## Conclusion




