#main.py

class HerokuApp:
    app_url = "https://fierce-spire-87558.herokuapp.com/"

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"start": "1970-01-01"}


@app.post("/method", status_code=201)
def root():
    return {"method": "POST"}


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