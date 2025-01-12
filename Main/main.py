from flight_data_processing import load_and_process_data
from flight_data_analysis import analyze_delays, max_delay, min_delay, sum_of_delays, most_occured_delay_time
from flight_data_visualization import plot_histogram


filepath = "/Users/aarushiyengar/Desktop/Programming/Python/Flight_Delay_Analysis/Airline_Delay_Cause.xlsx"

#Gets airline with the most flight delays
connection, data_frame = load_and_process_data(filepath)

filtered_data, most_delays_airline, total_delays = analyze_delays(connection)

plot_histogram(filtered_data)

print(f"The airline with the most delays is {most_delays_airline} with a delay time of {total_delays} minutes!")

cursor = connection.cursor()

# Average delay for a flight from the dataset
cursor.execute("SELECT AVG(late_aircraft_delay) FROM table_name")

avg_delay = cursor.fetchone()[0]

print(f"The average flight delay time is {avg_delay} minutes")

# Gets delay that took the most time
max_data = max_delay(connection)

print(f"The longest delay in this database is {max_data} minutes long")

#Gets delay that took the least time
min_data = min_delay(connection)

print(f"The delay the took the least amount was {min_data} minutes long")

#Sum of all delay(minutes)
sum_data = sum_of_delays(connection)

print(f"The sum of all delays in minutes is {sum_data}")


#Most occured delay time (mode)

mode_data = most_occured_delay_time(connection)

print(f"The most occured delay time is {mode_data} minutes")

connection.close()
