#main.py

# class HerokuApp:
#     app_url = "https://fierce-spire-87558.herokuapp.com/"

from fastapi import FastAPI
from pydantic import BaseModel

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

# class EventDetails(BaseModel):
#     date: str
#     event: str

# @app.put("/events", status_code=200)
# async def add_event(item: EventDetails, request: Request):
#     json_info = await request.json()
#     id = counter()

#     new_json = {
#         "date" : json_info["date"],
#         "name" : json_info["event"],
#         "date_added" : datetime.date.today().strftime,
#         "id" : id
#     }

    







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