#main.py

# class HerokuApp:
#     app_url = "https://fierce-spire-87558.herokuapp.com/"

from fastapi import FastAPI, Request, Response, status
from pydantic import BaseModel
import datetime
import collections


app = FastAPI()

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
def add_event(item: Item, request: Request):
    id = collections.Counter()

    calendar = {
        "date" : item["date"],
        "name" : item["event"],
        "date_added" : datetime.date.today().strftime,
        "id" : id
    }
    events = ()
    events.append(calendar)
    return calendar


    
# app.get("/event/{date}",status_code=200)
# async def event_on_date(date: str, response: Response):
#     if type(date) != str:
#         response.status_code = status.HTTP_400_BAD_REQUEST
#     else:
#         if date in event['date']:
#             return event
#         else:
#             response.status_code = status.HTTP_404_NOT_FOUND
#     return response.status_code