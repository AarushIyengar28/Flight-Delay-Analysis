import pandas as pd 
import sqlite3


def load_and_process_data(filepath):
    #Read data from excel which is the flight delay data
    data_frame = pd.read_excel(filepath, header = 1)


    #Prints the first 20 rows of data in the excel sheet
    #print(data_frame.head(20))

    connection = sqlite3.connect("flight_delays.db")

    data_frame.to_sql('table_name', connection, if_exists='replace', index = False)

    return connection, data_frame
