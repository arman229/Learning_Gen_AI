from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.bus import bus_routes, fare_details, schedule, helpline_info

app:FastAPI = FastAPI()

class RouteQuery(BaseModel):
    route_number: int

@app.post("/get_route_info")
async def get_route_info(query: RouteQuery):
    route_number = query.route_number
    if route_number in bus_routes:
        return {"route_number": route_number, "alignment": bus_routes[route_number]}
    else:
        raise HTTPException(status_code=404, detail="Route not found")




# @app.get("/get_fare_details")
# async def get_fare_details():
#     return fare_details

# @app.get("/get_schedule")
# async def get_schedule():
#     return schedule

# @app.get("/get_helpline_info")
# async def get_helpline_info():
#     return helpline_info

 