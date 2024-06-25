from openai.types.chat.chat_completion import ChatCompletionMessage, ChatCompletion
from openai import OpenAI
from src.openai_data import model, tool
from src.helper_fun import (
    find_lowest_fare_route,
    get_helpline_info,
    get_fare_details,
    get_schedule,
  
)
import json

client = OpenAI()


def run_conversation(prompt: str) -> str:
    messages = [{"role": "user", "content": prompt}]
    tools = tool
    response: ChatCompletion = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    response_message: ChatCompletionMessage = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        available_functions = {
            "find_lowest_fare_route": find_lowest_fare_route,
            "get_fare_details": get_fare_details,
            "get_schedule": get_schedule,
            "get_helpline_info": get_helpline_info,
         
        }
        messages.append(response_message)
        for tool_call in tool_calls:
            function_name = tool_call.function.name

            if function_name == "find_lowest_fare_route":
                function_to_call = available_functions[function_name]
                function_args = json.loads(tool_call.function.arguments)
                function_response = function_to_call(
                    start=function_args.get("start"),
                    end=function_args.get("end"),
                )
            elif function_name == "get_fare_details":
                function_to_call = available_functions[function_name]
                function_response = function_to_call()
            elif function_name == "get_schedule":
                function_to_call = available_functions[function_name]
                function_response = function_to_call()
            elif function_name == "get_helpline_info":
                function_to_call = available_functions[function_name]
                function_response = function_to_call()
            # elif function_name == "get_travel_information":
            #     function_to_call = available_functions[function_name]
            #     function_args = json.loads(tool_call.function.arguments)
            #     function_response = function_to_call(time=function_args.get("time"))

            else:
                continue

            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )

        second_response: ChatCompletion = client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return second_response.choices[0].message.content
