from flight_data_processing import load_and_process_data
import pandas as pd

def analyze_delays(connection):

    query = """
    SELECT * 
    FROM table_name 
    WHERE late_aircraft_delay > 0 AND late_aircraft_delay < 1000
    """

    filtered_data = pd.read_sql_query(query, connection)

    most_delays_airline = filtered_data.groupby("airport_name")['late_aircraft_delay'].sum().idxmax
    total_delays = filtered_data.groupby("airport_name")['late_aircraft_delay'].sum().max()

    return filtered_data, most_delays_airline, total_delays

def max_delay(connection):
    max_query = """
    SELECT MAX(late_aircraft_delay) 
    FROM table_name
"""
    max_data = pd.read_sql_query(max_query, connection)

    return max_data

def min_delay(connection):
    min_query = """
    SELECT MIN(late_aircraft_delay) 
    FROM table_name 
    WHERE late_aircraft_delay > 0
"""
    min_data = pd.read_sql_query(min_query, connection)

    return min_data

def sum_of_delays(connection):
    sum_query = """
    SELECT SUM(late_aircraft_delay) 
    FROM table_name
"""
    sum_data = pd.read_sql_query(sum_query, connection)

    return sum_data

def most_occured_delay_time(connection):
    mode_query = """
    SELECT late_aircraft_delay 
    FROM table_name 
    WHERE late_aircraft_delay > 0
    GROUP BY [late_aircraft_delay] 
    ORDER BY COUNT(*) DESC 
    LIMIT 1
"""
    mode_data = pd.read_sql_query(mode_query, connection)

    return mode_data
