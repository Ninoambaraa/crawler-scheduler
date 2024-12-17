import uvicorn 
from fastapi import FastAPI
from typing import Union
import requests 
import schedule
import time

app = FastAPI()  

@app.get("/")
async def read_root(): 
    return {"Hello": "World"}

@app.get("/scrape/queue")
async def scrape_queue(page: int):
    return {"page": page}

def hit_api(): 
    # Login first
    login_data = {
        "email": "johndoe@gmail.com",
        "password": "secret"
    }
    login_url = "https://c0c0c4s8sw8wcwwokcwwk0c8.84.247.149.184.sslip.io/auth/login"
    session = requests.Session()
    login_response = session.post(login_url, json=login_data)
    
    if login_response.status_code == 200:
        # After successful login, hit the scrape queue endpoint
        scrape_url = "http://localhost:8000/scrape/queue"
        params = {"page": 30}
        res = session.get(scrape_url, params=params)
        print(res.text)
        print(res.content)
    else:
        print(f"Login failed with status code: {login_response.status_code}")
        print(login_response.text)

# Schedule the API call every minute
schedule.every().minute.do(hit_api)
 
while True: 
    schedule.run_pending() 
    time.sleep(1)
