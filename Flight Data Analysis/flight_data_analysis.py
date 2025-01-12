from flight_data_processing import load_and_process_data
from pandas.plotting import table
import matplotlib.pyplot as plt
import pandas as pd

def analyze_delays(connection):

    query = """
    SELECT * FROM table_name WHERE late_aircraft_delay > 0 AND late_aircraft_delay < 1000
    """

    filtered_data = pd.read_sql_query(query, connection)

    most_delays_airline = filtered_data.groupby("airport_name")['late_aircraft_delay'].sum().idxmax
    total_delays = filtered_data.groupby("airport_name")['late_aircraft_delay'].sum().max()
    return filtered_data, most_delays_airline, total_delays
