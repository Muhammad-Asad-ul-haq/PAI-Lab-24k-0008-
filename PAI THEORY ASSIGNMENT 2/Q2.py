import numpy as np
with open("sensor_data.csv", "r") as file:
    x = file.readlines()

list = [line.strip().split(",") for line in x]
array = np.array(list)

array = np.array(list, dtype=float)
array[array == "-999"] = np.nan

array[(array < 0) | (array > 100)] = np.nan

MeanSensor = np.nanmean(array, axis=0)
print("First 10 values of Mean per sensor:", MeanSensor[:10])

MedianHour = np.nanmedian(array, axis=1)
print("First 10 values of Median per hour:", MedianHour[:10])

NanCount = np.isnan(array).sum(axis=0)
worst_sensor = np.argmax(NanCount)

print("Sensor with the most invalid readings:", worst_sensor)
print("Invalid count = ", NanCount[worst_sensor])

xmin = np.nanmin(array)
xmax = np.nanmax(array)
xnorm = (array - xmin) / (xmax - xmin)
print(xnorm)

np.savetxt("sensor_data_normalized.csv", xnorm)
