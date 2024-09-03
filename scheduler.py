import schedule
import time
import requests
from datetime import datetime

def hit_api():
    current_time = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Status Code: hi, Response: hi")
    

# Menjadwalkan tugas setiap 10 menit
schedule.every(1).minutes.do(hit_api)

while True:
    schedule.run_pending()
    time.sleep(1)
