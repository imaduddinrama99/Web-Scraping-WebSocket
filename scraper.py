import requests
from bs4 import BeautifulSoup
import json
import asyncio
import websockets

url = "https://realpython.github.io/fake-jobs/"

async def scrape_and_send():
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        jobs = soup.find_all("div", class_="card-content")

        data = []
        id_counter = 1

        for job in jobs:
            title = job.find("h2", class_="title").text.strip()
            company = job.find("h3", class_="company").text.strip()
            location = job.find("p", class_="location").text.strip()
            date = job.find("time").text.strip()

            item = {
                "id": id_counter,
                "title": title,
                "company": company,
                "location": location,
                "date": date
            }

            data.append(item)
            id_counter += 1

        # simpan ke JSON
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        # kirim ke websocket
        async with websockets.connect("ws://localhost:8765") as websocket:
            for item in data:
                await websocket.send(json.dumps(item))
                print("Dikirim:", item)

    else:
        print("Gagal scraping")

asyncio.run(scrape_and_send())