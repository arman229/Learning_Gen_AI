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
    