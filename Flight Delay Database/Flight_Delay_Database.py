import pandas as pd 
import sqlite3
import matplotlib.pyplot as plt

filepath = "/Users/aarushiyengar/Desktop/Programming/Python/Flight_Delay_Analysis/Airline_Delay_Cause.xlsx"
#Read data from excel which is the flight delay data
data_frame = pd.read_excel(filepath, header = 1)


#Prints the first 20 rows of data in the excel sheet
#print(data_frame.head(20))

connection = sqlite3.connect("flight_delays.db")

data_frame.to_sql('table_name', connection, if_exists='replace', index = False)



cursor = connection.cursor()

cursor.execute("PRAGMA table_info(table_name)")
columns = cursor.fetchall()

for column in columns:
    print(column)


#Queries data from the table we created that has a flight delaye ie late_aircraft_delay >0 and <1000(because we dont want outliers)
cursor.execute("SELECT * FROM table_name WHERE late_aircraft_delay > 0 AND late_aircraft_delay < 1000")

#Prints all the rows in the data that have flight delays
rows = cursor.fetchall()

for row in rows:
    print(row)


connection.close()
