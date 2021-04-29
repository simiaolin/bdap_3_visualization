import numpy as np
import matplotlib.pyplot as plt
import sys as sys
import pandas as pd

print(1)
distibution_file = "/Users/ary/dev/code/trait/bdap_3/src/resources/output/first/2010_03.trip_distribution"
ranges = []
cnts = []
with open(distibution_file) as file:
    for line in file:
        range_and_cnt = line.rstrip("\n")
        range = int(range_and_cnt.split(",")[0])
        cnt = int(range_and_cnt.split(",")[1])
        if (cnt < 200 and range < 30000):
            ranges.append(range)
            cnts.append(cnt)


file.close()
# plt.bar(ranges, cnts)

revenue_file = "/Users/ary/PycharmProjects/plotTaxiDistanceDistribution/revenue"
times = []
revenues = []
with open(revenue_file) as file:
    for line in file:
        time_and_revenue = line.rstrip("\n")
        time = time_and_revenue.split()[0]
        revenue = float(time_and_revenue.split()[1])
        times.append(time[2:])
        revenues.append(revenue)
plt.bar(times, revenues)
file.close()
# commutes = pd.Series(res)
# commutes.plot.hist(rwidth=0.9,
#                    color='#607c8e')
# plt.title('taxi trip dist distribution')
# plt.xlabel('trip length')
# plt.ylabel('counts')
# plt.grid(axis='y', alpha=0.75)
# ax2 = fig.add_subplot(122)
# todo add density and boxplot
plt.show()

#for bdap
# plt.yticks(np.arange(0.9, 1, 0.005))
# plt.xlabel("ensemble size")
# plt.ylabel("accuracy")
# ax2.set_ylim([0, 60])
# a = np.arange(1, 11)
# b = [0.919985,  0.918705, 0.945388, 0.946881, 0.953924, 0.954606, 0.95814,  0.958652, 0.960231, 0.960112]
# c = [59, 56.5, 56, 56, 55.6, 55.8, 55.6, 56.4, 55.2, 56]
# plt.plot(a, b, color="purple")
# plt.grid(axis='y', linestyle='-')
# # ax2.plot(a, c, color="pink")
#
# plt.show()