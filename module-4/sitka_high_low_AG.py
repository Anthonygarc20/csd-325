import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt


filename = 'sitka_weather_2018_simple.csv'

def plot_weather(type):
    """Handles the data extraction and plotting based on user choice."""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, temps = [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            
           
            if type == 'highs':
                temp = int(row[5])
                color = 'red'
                title = "Daily High Temperatures - 2018"
            else:
                temp = int(row[6])
                color = 'blue' # Requirement 6c: Lows must be blue
                title = "Daily Low Temperatures - 2018"
            
            temps.append(temp)

    # Visualization logic
    fig, ax = plt.subplots()
    ax.plot(dates, temps, c=color)

    # Format plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()


while True:
   
    print("\n--- Weather Data Menu ---")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")
    
    choice = input("Please select an option (1, 2, or 3): ")

    if choice == '1':
        plot_weather('highs')
    elif choice == '2':
        plot_weather('lows')
    elif choice == '3':
        
        print("Thank you for using the weather program. Goodbye!")
        sys.exit()
    else:
        print("Invalid selection. Please try again.")