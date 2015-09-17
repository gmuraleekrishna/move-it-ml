import matplotlib.pyplot as plt
import datetime
from matplotlib import dates as mpl_dates
hfmt = mpl_dates.DateFormatter('%m/%d')
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_locator(mpl_dates.MinuteLocator())
ax.xaxis.set_major_formatter(hfmt)
emails = []
dates = []
durations = []
dts = []
ax.set_ylim(bottom = 0)
with open('user_data.txt') as user_details:
    user_details_list = filter(None, user_details.read().split('\n'))
    for details in user_details_list:
        detail = details.split(' ')
        emails.append(detail[0])
        date = (datetime.datetime.strptime(detail[1], "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime(1970,1,1)).total_seconds()
        dates.append(date)
        durations.append(detail[2])
dts = map(datetime.datetime.fromtimestamp, dates)
fds = mpl_dates.date2num(dts)
print dates
ax.scatter(fds, durations)
plt.show()
