from fastapi import FastAPI, Request, HTTPException, Response, status, Cookie, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import datetime
import aiosqlite
import sqlite3
# conn = sqlite3.connect('northwind.db')
# conn.close()

app = FastAPI()
app.secret_key = "very constant and random secret, best 64+ characters"

@app.on_event("startup")
async def startup():
    app.db_connection = await aiosqlite.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")  # northwind specific


@app.on_event("shutdown")
async def shutdown():
    await app.db_connection.close()


@app.get("/suppliers", status_code = 200)
async def suppliers():
    cursor = await app.db_connection.cursor()
    app.db_connection.row_factory = aiosqlite.Row
    suppliersid_query = await cursor.execute("SELECT SupplierID, CompanyName FROM Suppliers ORDER BY SupplierID")
    suppliersid = await suppliersid_query.fetchall()
    return [{"SupplierID": x["SupplierID"], "CompanyName": x["CompanyName"]} for x in suppliersid]

@app.get("/suppliers/{id}", status_code = 200)
async def supplierss(id: int, response: Response):
    cursor = await app.db_connection.cursor()
    app.db_connection.row_factory = aiosqlite.Row
    suppliersid_query = await cursor.execute(f"SELECT * FROM Suppliers WHERE SupplierID = {id}")
    suppliersid = await suppliersid_query.fetchall()
    return id, suppliersid
    # if suppliersid is None:
    #     response.status_code = status.HTTP_200_OK
    # else:
    #     response.status_code = status.HTTP_404_NOT_FOUND

# app.access_tokens = []
# security = HTTPBasic()
# templates = Jinja2Templates(directory="templates/")

# @app.post('/check', response_class= HTMLResponse, status_code = 200)
# def login(response:Response, credentials: HTTPBasicCredentials = Depends(security)):
#     today = datetime.datetime.now()
#     birthdate = datetime.datetime.strptime(credentials.password, "%Y-%m-%d")
#     age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

#     if age >= 16:
#         return """<html>
#             <head>
#             </head>
#             <body>
#                 <h1>Welcome tester! You are 22</h1>
#             </body>
#             </html>"""
#     else:
#         response.status_code = status.HTTP_401_UNAUTHORIZED

# paths = []
# @app.put('/save/{pathh:path}', status_code =200)
# async def new_path(pathh: str, response:Response):
#     paths.append(pathh)
#     response.status_code = status.HTTP_200_OK




# # @app.post('/info')
# # def format(format: str, status_code_200, response:Response, response_class= HTMLResponse,):
# #     if format == 'json':
# #         return {"user_agent": "EDGE_UA"}
# #     elif format == 'html': """
# #         <html>
# #         <input type="text" id=user-agent name=agent value="{EDGE_UA}">
# #         </html>
# #         """
# #     else:
# #         response.status_code = status.HTTP_400_BAD_REQUEST



# # HTMLResponse(content=html_content, status_code=200)
# # if json:
























# @app.get('/start', response_class= HTMLResponse)
# def html():
#     return """
#     <html>
#         <head></head>
#         <body>
#             <h1>The unix epoch started at 1970-01-01</h1> 
#         </body>
#     </html>
#     """






















# app.counter = -1

# @app.get("/")
# def root():
#     return {"start": "1970-01-01"}

# @app.post("/method", status_code=201)
# def post():
#     return {"method": "POST"}

# @app.get("/method", status_code=200)
# def get():
#     return {"method": "GET"}

# @app.delete("/method", status_code=200)
# def delete():
#     return {"method": "DELETE"}

# @app.put("/method", status_code=200)
# def put():
#     return {"method": "PUT"}

# @app.options("/method", status_code=200)
# def options():
#     return {"method": "OPTIONS"}

# days = {1: "monday", 2: "tuesday", 3: "wednesday", 4: "thursday", 5: "friday", 6: "saturday", 7: "sunday"}

# @app.get("/day")
# def day(name: str, number: int, response: Response):
#     if number in days:
#         if days.get(number) == name:
#             return days[number]
#         else:
#             response.status_code = status.HTTP_400_BAD_REQUEST
#     else:
#         response.status_code = status.HTTP_400_BAD_REQUEST


# class Item(BaseModel):
#     date: str
#     event: str

# @app.put("/events", status_code=200)
# def add_event(item: Item):
#     app.counter += 1
#     global cal
#     global events

#     cal = {
#         "id" : app.counter,
#         "name" : item.event,
#         "date" : item.date,
#         "date_added" : datetime.date.today().strftime("%Y-%m-%d"),
#     }
    
#     events = []
#     events.append(cal)

#     return cal


# @app.get("/events/{date}", status_code=200)
# def event_on_date(date: str, response: Response):
#     try:
#         datetime.datetime.strptime(date, "%Y-%m-%d")
#     except ValueError:
#         response.status_code = status.HTTP_400_BAD_REQUEST
#     else:
#         for e in events:
#             if date == e['date']:    
#                 return events
#             else:
#                 response.status_code = status.HTTP_404_NOT_FOUND
    
# app.get("/events/{date}",status_code=200)
# def event_date(date: str, response: Response):
    # try:
    #     datetime.datetime.strptime(date, "%Y-%m-%d")
    # except:
    #     response.status_code = status.HTTP_400_BAD_REQUEST
    #     return "Nope"

    # for i, event in enumerate(events):
    #     if date == event['date']:
    #         index = i

    # if index is not None:
    #     return events[index]
    # else:
    #     response.status_code = status.HTTP_404_NOT_FOUND


