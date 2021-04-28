import csv

reader1 = csv.reader(open("2021-04-26_dht22_sensor_3660.csv"), delimiter=";")
reader2 = csv.reader(open("2021-04-26_sds011_sensor_3659.csv"), delimiter=";")

print("DHT22:")
for row in reader1:
	print(row)

print("SDS011:")
for row in reader2:
	print(row)