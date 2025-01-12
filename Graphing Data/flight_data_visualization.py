from flight_data_processing import load_and_process_data
import sqlite3
import matplotlib.pyplot as plt


#Graphing the late aircraft delay data through matplotlib with a histogram

#Filtered data makes sure that the delays are between an amount of minutes you want ie for this it is 0< and <100
def plot_histogram(filtered_data):

    plt.figure(figsize=(10,6))
    plt.hist(filtered_data['late_aircraft_delay'], bins = 50, color = 'skyblue', edgecolor = 'skyblue')
    plt.title("Distribution of late aircraft delays")
    plt.xlabel("Late Aircraft Delay(Minutes)")
    plt.ylabel("Frequency")
    plt.show()
#The data is skewed right because almost all of the delays are below 1000 minutes long and the others are just outliers
#The data is skewed right because almost all of the delays are below 1000 minutes long and the others are just outliers
