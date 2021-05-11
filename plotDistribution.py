import matplotlib.pyplot as plt
import sys as sys

#plot distribution of trip length
def plotTripLengthDistribution(trip_distribution_file):
    trip_length = []
    count_of_length = []
    with open(trip_distribution_file) as file:
        for line in file:
            length_and_count = line.rstrip("\n")
            trip_length.append(int(length_and_count.split(",")[0]))
            count_of_length.append(int(length_and_count.split(",")[1]))
    file.close()
    plt.bar(trip_length, count_of_length)
    plt.show()

#plot distribution of airport revenue
def plotAirportTripRevenueDistribution(airport_trip_revenue_file):
    times = []
    revenues = []
    with open(airport_trip_revenue_file) as file:
        for line in file:
            time_and_revenue = line.rstrip("\n")
            time = time_and_revenue.split()[0]
            revenue = float(time_and_revenue.split()[1])
            times.append(time)
            revenues.append(revenue)

    plt.bar(times, revenues)
    plt.xticks(rotation=-30, size=8)  # 设置x轴标签旋转角度
    file.close()
    plt.show()


type = sys.argv[1]
if (type == 'trip_length'):
    plotTripLengthDistribution(sys.argv[2])
elif (type == 'trip_revenue'):
    plotAirportTripRevenueDistribution(sys.argv[2])
else:
    print("the plotting type should be [trip_length]  or [trip_revenue]")

