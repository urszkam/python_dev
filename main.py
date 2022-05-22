#main.py

# class HerokuApp:
#     app_url = "https://fierce-spire-87558.herokuapp.com/"

from fastapi import FastAPI, Request, Response, status
from pydantic import BaseModel
import datetime
from collections import Counter


app = FastAPI()
app.counter = -1

@app.get("/")
def root():
    return {"start": "1970-01-01"}

@app.post("/method", status_code=201)
def post():
    return {"method": "POST"}

@app.get("/method", status_code=200)
def get():
    return {"method": "GET"}

@app.delete("/method", status_code=200)
def delete():
    return {"method": "DELETE"}

@app.put("/method", status_code=200)
def put():
    return {"method": "PUT"}

@app.options("/method", status_code=200)
def options():
    return {"method": "OPTIONS"}

days = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}

@app.get("/day")
def day(name: str, number: int, response: Response):
    if number in days:
        if days.get(number) == name:
            return days[number]
        else:
            response.status_code = status.HTTP_400_BAD_REQUEST
    else:
        response.status_code = status.HTTP_400_BAD_REQUEST


class Item(BaseModel):
    date: str
    event: str

@app.put("/events", status_code=200)
def add_event(item: Item):
    app.counter += 1
    global calendar

    calendar = {
        "id" : app.counter,
        "name" : item.event,
        "date" : item.date,
        "date_added" : datetime.date.today().strftime("%Y-%m-%d"),
    }
    
    global events
    events = []
    events.append(calendar)

    return calendar


    
app.get("/events/{date}",status_code=200)
def event_date(date: str, response: Response):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return "Nope"

    if date in calendar['date']:
        return events
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
