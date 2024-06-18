from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.bus import routes
from queue import Queue
app:FastAPI = FastAPI()


@app.get("/fun_calling")
def fun_calling():
    final=fun_calling("i want to travel from 'R.A Bazar'' to 'Nadeem Chowk'")
    print(final)
 
import os
from dotenv import load_dotenv,find_dotenv
from openai import OpenAI
import json

__: bool =  load_dotenv(find_dotenv())

client:OpenAI = OpenAI()
import requests
import json
def find_lowest_fare_route(start: str, end: str):
    url = "http://127.0.0.1:8000/find_lowest_fare_route"
    payload = {"start": start, "end": end}
    response = requests.post(url, json=payload)
    return response.json()
def fun_calling(prompt:str):
    messages    = [{
        "role": "user",
        "content": prompt,
    }]
    tools= [
    {
        "type": "function",
        "function": {
            "name": "find_lowest_fare_route",
            "description": "Find the lowest fare route between two stops",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {
                        "type": "string",
                        "description": "The starting stop, e.g. 'A'"
                    },
                    "end": {
                        "type": "string",
                        "description": "The ending stop, e.g. 'E'"
                    },
                },
                "required": ["start", "end"],
            },
        },
    }]
    model = "gpt-3.5-turbo-1106"
    response = client.chat.completions.create(
    model=model,
    messages=messages,
    tools=tools,
    max_tokens=200,
    
)

    fun_response = response.choices[0].messages
    tools_response = fun_response.tools_calls
    if tools_response:
        available_function ={
            "find_lowest_fare_route":find_lowest_fare_route,
        }
        messages.append(fun_response)
        for tools_data in tools_response:
            function_name = tools_data.function.name
            function_args = json.loads(tools_data.function.arguments)
           
    
            function_response = available_function[function_name](**function_args)
            messages.append(
            {
                "tool_call_id": tools_data.id,
                "role": "tool",
                "content": function_response,
                "name":function_response,
            }
            )
        final_response =client.chat.compoletions.create(
            model=model,
            messages=messages
        )    
        return final_response.choices[0].message.content
     
 
 
 
@app.get("/find_shortest_distance_route")
def find_shortest_distance_route(start, end):
    q = Queue()
    q.put((start, [])) 
    visited = set()
    while not q.empty():
        current_stop, path_taken = q.get()
        if current_stop == end:
            return path_taken + [end]
        if current_stop in visited:
            continue
        visited.add(current_stop)
        for route_name, route_data in routes.items():
            stops = route_data['stops']
            if current_stop in stops:
                index = stops.index(current_stop)
                for next_stop in stops[index + 1:]:
                    if next_stop not in visited:
                        q.put((next_stop, path_taken + [current_stop]))
                for prev_stop in reversed(stops[:index]):
                    if prev_stop not in visited:
                        q.put((prev_stop, path_taken + [current_stop]))
    
    return None   
@app.get("/find_lowest_fare_route")
def find_lowest_fare_route(start, end):
    q = Queue()
    q.put((start, [], 0))   
    visited = set()
    min_fare = float('inf')
    best_path = None
    while not q.empty():
        current_stop, path_taken, total_fare = q.get()
        if current_stop == end:
            if total_fare < min_fare:
                min_fare = total_fare
                best_path = path_taken + [end]
            continue
        if current_stop in visited:
            continue
        visited.add(current_stop)
        for route_name, route_data in routes.items():
            stops = route_data['stops']
            fare = route_data['fare']
            if current_stop in stops:
                index = stops.index(current_stop)
                for i in range(index + 1, len(stops)):
                    next_stop = stops[i]
                    if next_stop not in visited:
                        q.put((next_stop, path_taken + [current_stop], total_fare + fare))
                for i in range(index - 1, -1, -1):
                    prev_stop = stops[i]
                    if prev_stop not in visited:
                        q.put((prev_stop, path_taken + [current_stop], total_fare + fare))
    return best_path, min_fare


 
start = 'UMT Stop'
end = 'Kalma Chowk'
 
shortest_distance_path = find_shortest_distance_route(start, end)
if shortest_distance_path:
    print(f"Shortest Distance Route: {shortest_distance_path}")
 
lowest_fare_path, fare = find_lowest_fare_route(start, end)
if lowest_fare_path:
    print(f"Lowest Fare Route: {lowest_fare_path}")
    print(f"Fare: Rs {fare}")


# @app.get("/get_fare_details")
# async def get_fare_details():
#     return fare_details

# @app.get("/get_schedule")
# async def get_schedule():
#     return schedule

# @app.get("/get_helpline_info")
# async def get_helpline_info():
#     return helpline_info

 