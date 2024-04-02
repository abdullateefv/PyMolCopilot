"""
Stores functions to run and process conversations with OpenAI API for GPT
"""

import json
import os
import re

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionMessage

from backend.appearanceFunctions import bgColor_cmd, cartoon_cmd, refresh_cmd
<<<<<<< Updated upstream
from backend.moleculeCRUDFunctions import create_cmd, bond_cmd, protect_cmd, attach_cmd, center
=======
from backend.moleculeCRUDFunctions import create_cmd, bond_cmd, protect_cmd, attach_cmd, center_cmd
>>>>>>> Stashed changes
from backend.viewFunctions import origin_cmd, backward_cmd
from backend.settingsFunctions import button_cmd

# Load API Key from .env file
load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)

def run_conversation(newMessage, verbose):
    """
    Executes a conversation with the OpenAI API and returns the message history object.
    Allows for up to two messages from the API, one responding to the initial request with optional function calls
    and another after receiving data from function calls if made.

    Parameters
    ----------
    newMessage : str
        Prompt from user
    verbose : bool
        Specifies if Copilot should always send a textual message or just the function call details

    Returns
    -------
    message_history : str
        Literal chat content with user prompt, copilot response, function calls processed and styled by helper functions
    """

    # Step 1: Adds verbosity instruction if desired
    if verbose: newMessage += " Always acknowledge the message, always send content not just a function call at all steps"

    # Step 2: Sends user's newMessage prompt and description of available function tools to GPT with usage details
    messages = [{"role": "user", "content": newMessage}]

    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    tools_desc_path = os.path.join(parent_dir, 'backend', 'toolsDescription.json')
    with open(tools_desc_path, 'r') as f:
        tools = json.load(f)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    # Step 3: Retrieves initial response from GPT and appends to message history
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    messages.append(response_message)

    # Step 4: Check if the model wanted to call a function
    if tool_calls:

        # Step 7: Call the desired functions
        # TODO: MUST UPDATE THIS WHEN NEW FUNCTIONS ARE ADDED
        available_functions = {
            "origin_cmd": origin_cmd,
            "bgColor_cmd": bgColor_cmd,
            "cartoon_cmd": cartoon_cmd,
            "bond_cmd": bond_cmd,
            "create_cmd": create_cmd,
            "protect_cmd": protect_cmd,
            "refresh_cmd": refresh_cmd,
            "attach_cmd": attach_cmd,
            "button_cmd": button_cmd,
            "backward_cmd": backward_cmd,
<<<<<<< Updated upstream
            "center": center, 
=======
            "center_cmd": center_cmd,
>>>>>>> Stashed changes
        }

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)

            # Step 8: Append returned values from called functions to message history
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )

        # Step 9: Return message history updated with called function returned values to GPT for it to analyze
        second_response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
        )

        # Step 10: Append GPT's response after receiving triggered function data to message history
        response_message = second_response.choices[0].message
        messages.append(response_message)

        # Step 11: Process message history into chat format and format for return
        return style_messages(process_messages(messages, verbose))


def process_messages(messages, verbose):
    """
    Processes JSON-style message history of GPT conversation from run_conversation() to the literal textual chat content

    Parameters
    ----------
    messages : list
        JSON-style message history of GPT conversation as a List of dictionary or ChatCompletionMessage objects
    verbose : bool
        Specifies if Copilot should always send a textual message or just the function call details

    Returns
    -------
    processed_messages : str
        Literal chat style processed messages to be displayed
    """
    processed_messages = []
    tool_call_requests = []  # To store details about the tool calls
    tool_call_responses = {}  # To map responses to their calls

    # First, categorize messages and collect tool call responses
    for message in messages:
        if isinstance(message, dict) and message['role'] == 'tool':
            tool_call_responses[message['tool_call_id']] = message

    for message in messages:
        if isinstance(message, ChatCompletionMessage):
            # Process the initial assistant message and any subsequent ones
            processed_messages.append(f"\nAssistant:\n{message.content}")

            # After the first assistant message, process any tool call requests
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_call_requests.append(tool_call)
                    tool_call_id = tool_call.id
                    if tool_call_id in tool_call_responses:
                        tool_response = tool_call_responses[tool_call_id]
                        tool_content = json.loads(tool_response['content'])
                        arguments = json.loads(tool_call.function.arguments)
                        processed_messages.append(
                            f'\nTool Call: "{tool_call.function.name}"; Arguments: {arguments}"; Returned: {tool_content}\n'
                        )

        elif isinstance(message, dict) and message['role'] == 'user':
            if verbose:
                processed_messages.append(f"\nUser:\n{message['content'][:-90]}")
            else:
                processed_messages.append(f"\nUser:\n{message['content']}")

    return "\n".join(processed_messages)


def style_messages(messages):
    """
    Styles the chat content by adding HTML tags to the messages
    Wraps 'User' and 'Assistant' in bold. Replaces ANSI style /n characters with HTML style <br>

    Parameters
    ----------
    messages : str
        Stringified literal chat content from process_messages

    Returns
    -------
    styled_messages : str
        Stringified literal chat content with HTML tags added for styling
    """
    pattern = r'(Assistant:|User:)'
    styled_messages = re.sub(pattern, r'<b>\1</b>', messages)
    styled_messages = styled_messages.replace('\n', '<br>')

    return styled_messages
