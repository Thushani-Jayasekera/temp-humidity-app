import csv
import time
import random

while True:
    for sector in ['sector1', 'sector2', 'sector3']:
        filename = f'/readings/soil_humity_readings_sector_{sector}.csv'
        with open(filename, 'a') as file:
            writer = csv.writer(file)
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
            humidity = random.uniform(100, 500)
            writer.writerow([current_time, humidity])
    time.sleep(5)