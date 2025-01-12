from flight_data_processing import load_and_process_data
from flight_data_analysis import analyze_delays
from flight_data_visualization import plot_histogram


filepath = "/Users/aarushiyengar/Desktop/Programming/Python/Flight_Delay_Analysis/Airline_Delay_Cause.xlsx"

connection, data_frame = load_and_process_data(filepath)

filtered_data, most_delays_airline, total_delays = analyze_delays(connection)

plot_histogram(filtered_data)

print(f"The airline with the most delays is {most_delays_airline} with a delay time of {total_delays} minutes!")

connection.close()
