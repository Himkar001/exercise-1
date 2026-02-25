# Weather and AQI data analysis for Gandhinagar (last 10 days)
# Calculates average and median and stores results in a text file

import statistics

# Sample data for last 10 days
temperature = [32, 33, 31, 34, 35, 36, 34, 33, 32, 31]
humidity = [45, 48, 50, 47, 46, 44, 43, 45, 49, 51]
aqi = [92, 95, 90, 98, 105, 110, 108, 100, 96, 94]

# Calculate averages
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)
avg_aqi = sum(aqi) / len(aqi)

# Calculate medians
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)
median_aqi = statistics.median(aqi)

# Store results in a text file
with open("analysis_results.txt", "w") as file:
    file.write("Weather and AQI Data Analysis for Gandhinagar (Last 10 Days)\n")
    file.write("-----------------------------------------------------------\n")
    file.write(f"Average Temperature: {avg_temp:.2f} °C\n")
    file.write(f"Median Temperature : {median_temp} °C\n\n")
    file.write(f"Average Humidity   : {avg_humidity:.2f} %\n")
    file.write(f"Median Humidity    : {median_humidity} %\n\n")
    file.write(f"Average AQI        : {avg_aqi:.2f}\n")
    file.write(f"Median AQI         : {median_aqi}\n")

print("Analysis completed. Results saved to 'analysis_results.txt'.")
