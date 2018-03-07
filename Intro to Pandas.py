import pandas as pd
import numpy as np
s = pd.Series([1,3,5,np.nan,6,8])
s

dates = pd.date_range('20130101', periods=6)

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

df2.describe()

df2.dtypes
df2.corr()
df2.all
df2.D
df2.<TAB>


df2.std()

df2.head()

df.index

df.columns

df.values

df.T # Transposing data

df.sort_index(axis=1,ascending=False )
df.sort_values(by='B')

df['A']

df[0:3]

df.loc[dates]

df.loc[:,['A','B']]

df.iloc[3]
df.iloc[[1,2,4],[0,2]]
df.iloc[[1,2,3],:]
df[df.A > 0]

df[df.B <0]

df.iat[0,1] = 0

df2 = df.copy()
df2['E'] = ['One','One','Two','Three','Four','Three']
df2[df2['E'].isin(['Two', 'Four'])]

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))

df.at[dates[0],'A'] = 0
df2 = df.copy()
df2[df2 > 0] = -df2

df2
df.loc[:,'D'] = np.array([5] * len(df))

df



# import datetime
# import pandas.io.data as web
# import matplotlib.pyplot as plt
# from matplotlib import style
# from pandas_datareader import data, wb
#
# style.use('ggplot')
#
# start = datetime.datetime(2015,1,1)
# end = datetime.datetime(2018,1,1)
#
# df = web.datareader("XOM", "yahoo", start, end)
#
# print(df.head())
#
# df['Adj Close'].plot()
#
# plt.show()
#

