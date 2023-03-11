import csv
import time
import random

while True:
    for sector in ['sector1', 'sector2', 'sector3']:
        filename = f'/readings/soil_temprature_readings_sector_{sector}.csv'
        with open(filename, 'a') as file:
            writer = csv.writer(file)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            temperature = random.uniform(10, 120)
            writer.writerow([current_time, temperature])
    time.sleep(5)


#temprature sensor read - 1 pod - for loop for each secotor and insert to a csv file
#humidity sensor read - "
# user request  - flask app - csv file read and send according to sectror[2
