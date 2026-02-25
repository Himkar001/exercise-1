# Weather and AQI data analysis for Gandhinagar (last 10 days)
# Calculates average and median of temperature, humidity, and AQI

import statistics

# Sample data for last 10 days
# Temperature in Celsius, Humidity in %, AQI as index value

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

# Display results
print("Weather and AQI Data Analysis for Gandhinagar (Last 10 Days)")
print("-----------------------------------------------------------")
print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Median Temperature : {median_temp} °C")
print()
print(f"Average Humidity   : {avg_humidity:.2f} %")
print(f"Median Humidity    : {median_humidity} %")
print()
print(f"Average AQI        : {avg_aqi:.2f}")
print(f"Median AQI         : {median_aqi}")
