import csv

reader = csv.DictReader(open("2021-04-26_dht22_sensor_3660.csv"), delimiter=";")

for row in reader:
	print("Zeit: ", row["timestamp"], " Temperatur: ", row["temperature"])
