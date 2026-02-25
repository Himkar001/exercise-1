# Weather data analysis for Gandhinagar (last 10 days)
# Calculates average and median of temperature and humidity

import statistics

# Sample weather data for last 10 days
# Temperature in Celsius, Humidity in percentage

temperature = [32, 33, 31, 34, 35, 36, 34, 33, 32, 31]
humidity = [45, 48, 50, 47, 46, 44, 43, 45, 49, 51]

# Calculate averages
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)

# Calculate medians
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)

# Display results
print("Weather Data Analysis for Gandhinagar (Last 10 Days)")
print("--------------------------------------------------")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Median Temperature : {median_temp} °C")
print(f"Average Humidity   : {avg_humidity:.2f} %")
print(f"Median Humidity    : {median_humidity} %")
