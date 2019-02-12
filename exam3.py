import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web

start = datetime.datetime(2018,2,1)
end = datetime.datetime(2018,2,15)

gs_c = web.DataReader('C', 'iex', start, end)

print(gs_c)

fig = plt.figure('Test Chart')
fig.set_size_inches(10, 6, forward=True)

plt.plot(gs_c.index, gs_c['high'], 'r')
plt.show()
