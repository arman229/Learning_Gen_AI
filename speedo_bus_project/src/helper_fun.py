from queue import Queue
import json   
from fuzzywuzzy import fuzz
from src.routes_data import routes,fare_details,helpline_info,schedule
 

def find_lowest_fare_route(start, end):
    threshold = 85   
    def find_best_match(stop_name):
        best_match = None
        best_score = 0
        for route_name, route_data in routes.items():
            stops = route_data['stops']
            for stop in stops:
                score = fuzz.token_sort_ratio(stop.lower(), stop_name.lower())
                if score > threshold and score > best_score:
                    best_score = score
                    best_match = stop
        return best_match
    
   
    start = find_best_match(start)
    end = find_best_match(end)
    
    if not start or not end:
        return "I'm sorry, but it appears that there is no direct route between {} and {}.".format(start or "your starting stop", end or "your destination")
    
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
    
    if best_path:
        return json.dumps({"best_path": best_path, "min_fare": min_fare})
    else:
        return "I'm sorry, but it appears that there is no direct route between {} and {}.".format(start, end)
    
    
    
    
    
def get_fare_details() -> dict:
    
    return json.dumps(fare_details)
def get_schedule() -> dict:
  
    return json.dumps(schedule) 
def get_helpline_info() -> dict:
    
    return json.dumps(helpline_info)
# def get_travel_information(time):
    
#     schedule = {
#         "start_time": 6,   
#         "end_time": 22,   
#         "frequency": "5 to 10 minutes"
#     }
     
#     time_hour = int(time.split()[0].split(':')[0])
#     time_period = time.split()[1]
#     if time_period.lower() == 'pm' and time_hour != 12:
#         time_hour += 12
#     elif time_period.lower() == 'am' and time_hour == 12:
#         time_hour = 0
 
#     if schedule["start_time"] <= time_hour < schedule["end_time"]:
#         return "You can travel at this time using the Speedo bus."
#     else:
#         return "You can't travel at this time using the Speedo bus, but you can book a ride online."
