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


def plot_pie_chart(top_ten_airlines):
    #used dropna to drop all non available values (nan)
    top_ten_airlines = top_ten_airlines.dropna(subset=['airport'])
    top_ten_airlines['airport'] = top_ten_airlines['airport'].str.strip()
    
    # used .loc to avoid warning with none numeric values
    top_ten_airlines.loc[:, 'Percentage'] = top_ten_airlines['Percentage'].astype(float)
    
    # check if the percentages sum more than 1, and normalize them
    total_percentage = top_ten_airlines['Percentage'].sum()
    if total_percentage > 1:
        print(f"Warning: The sum of percentages is {total_percentage}. Normalizing...")
        top_ten_airlines['Percentage'] = top_ten_airlines['Percentage'] / total_percentage
    
    print("Sum of percentages:", top_ten_airlines['Percentage'].sum())
    
    # Plotting the pie chart
    plt.figure(figsize=(10, 8))
    plt.pie(
        top_ten_airlines['Percentage'],
        labels=top_ten_airlines['airport'],
        autopct='%1.1f%%',  # show percentages with 1 decimal place
        startangle=140,
        textprops={'fontsize': 10}
    )
    plt.axis('equal')  # makes sure it is a circle and not a ellipse
    plt.show()
