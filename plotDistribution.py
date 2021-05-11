import matplotlib.pyplot as plt
import sys as sys

#plot distribution of trip length in unit m
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
    plt.xlabel('trip length (meter)', fontsize=12)
    plt.ylabel('count', fontsize=12)
    plt.title('Trip Length Distribution', fontsize=20, pad=20)
    plt.show()

#plot distribution of trip length in unit km
def plotTripLengthDistributionInUnitKM(trip_distribution_file):
    trip_distribution_dist = {}
    with open(trip_distribution_file) as file:
        for line in file:
            length_and_count = line.rstrip("\n")
            current_trip_lenght = int(length_and_count.split(",")[0])
            current_count_of_length = int(length_and_count.split(",")[1])
            trip_length_in_km = round(current_trip_lenght / 1000)
            if trip_length_in_km in trip_distribution_dist:
                trip_distribution_dist[trip_length_in_km] +=  current_count_of_length
            else:
                trip_distribution_dist[trip_length_in_km] = current_count_of_length
    file.close()

    x = []
    y = []
    for trip_length_in_km in trip_distribution_dist:
        x.append(trip_length_in_km)
        y.append(trip_distribution_dist[trip_length_in_km])
    plt.bar(x, y)
    plt.xlabel('trip length (kilo meter)', fontsize=12)
    plt.ylabel('count', fontsize=12)
    plt.title('Trip Length Distribution',fontsize=20, pad=20)
    plt.show()


#plot distribution of airport revenue
def plotAirportTripRevenueDistribution(airport_trip_revenue_file):
    times = []
    revenues = []
    total_revenue = 0
    with open(airport_trip_revenue_file) as file:
        for line in file:
            time_and_revenue = line.rstrip("\n")
            time = time_and_revenue.split()[0]
            revenue = float(time_and_revenue.split()[1])
            times.append(time)
            revenues.append(revenue)
            total_revenue += revenue

    plt.bar(times, revenues)
    plt.xticks(rotation=-30, size=8)  # 设置x轴标签旋转角度
    plt.xlabel('time (year_and_month)', fontsize=12)
    plt.ylabel('revenue (dollar)', fontsize=12)
    plt.title('Airport Ride Revenue',fontsize=20, pad=20)
    print("total revenue " + str(total_revenue))
    file.close()
    plt.show()


type = sys.argv[1]
if (type == 'trip_length'):
    plotTripLengthDistribution(sys.argv[2])
elif (type == 'trip_length_in_km'):
    plotTripLengthDistributionInUnitKM(sys.argv[2])
elif (type == 'trip_revenue'):
    plotAirportTripRevenueDistribution(sys.argv[2])
else:
    print("the plotting type should be [trip_length] or [trip_length_in_km] or [trip_revenue]")

