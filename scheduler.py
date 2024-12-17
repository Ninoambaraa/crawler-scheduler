import schedule
import time
import requests
from datetime import datetime

def hit_api():
    res = requests.get("https://c0c0c4s8sw8wcwwokcwwk0c8.84.247.149.184.sslip.io")

    print(res.text)  
    print(res.content)

    current_time = datetime.now().strftime("%A, %Y-%m-%d %H:%M:%S")
    print(f"[{current_time}] Status Code: RUN CRAWLING !")

schedule.every(1).minutes.do(hit_api)

while True:
    schedule.run_pending()
    time.sleep(1)