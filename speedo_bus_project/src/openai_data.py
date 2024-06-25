tool = [
    {
        "type": "function",
        "function": {
            "name": "find_lowest_fare_route",
            "description": " Determines the lowest fare route between two specified bus stops using the Speedo bus service. This function helps passengers find the most cost-effective path from their starting stop to their destination stop.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {
                        "type": "string",
                        "description": "The starting stop, e.g. 'A'",
                    },
                    "end": {
                        "type": "string",
                        "description": "The ending stop, e.g. 'E'",
                    },
                },
                "required": ["start", "end"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_fare_details",
            "description": "Provides detailed fare information for the Speedo bus service. This includes the cost of tickets, which is crucial for passengers planning their travel expenses.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_schedule",
            "description": " Retrieves the schedule for Speedo buses, including the start and end times of service and the frequency of buses. The Speedo buses operate from 6 AM to 10 PM, with a bus arriving every 5 to 10 minutes. This information helps passengers plan their trips and ensures they can catch a bus at their desired time.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_helpline_info",
            "description": "Provides the helpline contact information for the Speedo bus service. Passengers can use this helpline number to get assistance, make inquiries, or report issues related to their travel.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        },
    },
    # {
    #     "type": "function",
    #     "function": {
    #         "name": "get_travel_information",
    #         "description": "Determines if travel is possible using the Speedo bus service at a specified time. Checks if the travel time is within the service schedule (6 AM to 10 PM). Handles various time formats.",
    #         "parameters": {
    #             "type": "object",
    #             "properties": {
    #                 "time": {
    #                     "type": "string",
    #                     "description": "The desired travel time, e.g., '12 PM' or '12pm'.",
    #                 }
    #             },
    #             "required": ["time"],
    #         },
    #     },
    # },
]

model = "gpt-3.5-turbo-1106"
