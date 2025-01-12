from Flight_Delay_Database import data_frame
import sqlite3
import matplotlib.pyplot as plt

#Graphing the late aircraft delay data through matplotlib with a histogram
plt.figure(figsize=(10,6))
plt.hist(data_frame['late_aircraft_delay'], bins = 50, color = 'skyblue', edgecolor = 'skyblue')
plt.title("Distribution of late aircraft delays")
plt.xlabel("Late Aircraft Delay(Minutes)")
plt.ylabel("Frequency")
plt.show()
#The data is skewed right because almost all of the delays are below 1000 minutes long and the others are just outliers
