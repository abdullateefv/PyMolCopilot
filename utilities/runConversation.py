"""
Stores functions to run and process conversations with OpenAI API for GPT
"""

import json
import os
import re
from dotenv import load_dotenv
from openai import OpenAI
from pymol import cmd
from openai.types.chat import ChatCompletionMessage
from backend.appearanceFunctions import bgColor_cmd, cartoon_cmd, refresh_cmd, color_cmd
from backend.moleculeCRUDFunctions import create_cmd, bond_cmd, protect_cmd, attach_cmd, remove_cmd, delete_cmd, \
    center_cmd, h_fill_cmd, indicate_cmd, invert_cmd, disable_cmd
from backend.viewFunctions import origin_cmd, backward_cmd, quit_cmd, index_cmd, move_cmd, orient_cmd
from backend.settingsFunctions import button_cmd

from colorama import Fore, Style, init

# Set up pretty console printer
init(autoreset=True)
os.system('color')

# Load API Key from .env file
load_dotenv()
api_key = os.getenv('API_KEY')
client = OpenAI(api_key=api_key)


def fetch_cmd(pdb_code):
    try:
        cmd.fetch(pdb_code)
        return json.dumps({'success': True})
    except Exception as e:
        return json.dumps({'success': False})


# Define available functions for calling
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
    "color_cmd": color_cmd,
    "quit_cmd": quit_cmd,
    "remove_cmd": remove_cmd,
    "delete_cmd": delete_cmd,
    "center_cmd": center_cmd,
    "h_fill_cmd": h_fill_cmd,
    "index_cmd": index_cmd,
    "indicate_cmd": indicate_cmd, 
    "disable_cmd": disable_cmd,
    "invert_cmd": invert_cmd,
    "move_cmd": move_cmd,
    "orient_cmd": orient_cmd
}

# Load toolsDescription.json defining available function tools
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
tools_desc_path = os.path.join(parent_dir, 'backend', 'toolsDescription.json')
with open(tools_desc_path, 'r') as f:
    tools = json.load(f)


def run_conversation(newMessage):
    """
    Executes a conversation with the OpenAI API and returns the message history object.
    Allows for up to two messages from the API, one responding to the initial request with optional function calls
    and another after receiving data from function calls if made.

    Parameters
    ----------
    newMessage : str
        Prompt from user

    Returns
    -------
    message_history : str
        Literal chat content with user prompt, copilot response, function calls processed and styled by helper functions
    """

    # Chat setup and add model instructions
    messages = []
    messages.append({"role": "system", "content": "Don't make assumptions about what values to plug into functions. "
                                                  "Ask for clarification if a user request is ambiguous."})
    messages.append({"role": "system",
                     "content": "If you are not sure about which molecule PDB ID to load for the fetch command and there are multiple possible options, ask for clarification. For example, whole structure versus one domain."})
    messages.append({"role": "user", "content": newMessage})

    # Get intial model response
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    messages.append(response_message)

    # While the model is making tool calls
    while tool_calls:
        # Handle each tool call
        for tool_call in tool_calls:
            function_to_call = available_functions[tool_call.function.name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(**function_args)
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": tool_call.function.name,
                    "content": function_response,
                }
            )

        # Ask model if it would like ot make more tool calls
        messages.append({"role": "system",
                         "content": "If there any more tools/functions to be called to satisfy the user's prompt that have not been called already, call/invoke them. Otherwise, summarize what has just been done for the user"})

        # Get response
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=messages,
            tools=tools,
            tool_choice="auto",
        )

        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls
        messages.append(response_message)

    return messages


def process_messages(messages):
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
    toolCallsResults = []

    # First, categorize messages and collect tool call responses
    for message in messages:
        if isinstance(message, dict) and message['role'] == 'tool':
            tool_call_responses[message['tool_call_id']] = message

    for message in messages:
        if isinstance(message, ChatCompletionMessage):
            # Process the initial assistant message and any subsequent ones
            processed_messages.append("\nAssistant:")
            if message.content is not None:
                processed_messages.append(f"{message.content}")

            # After the first assistant message, process any tool call requests
            if message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_call_requests.append(tool_call)
                    tool_call_id = tool_call.id
                    if tool_call_id in tool_call_responses:
                        tool_response = tool_call_responses[tool_call_id]
                        tool_content = json.loads(tool_response['content'])
                        arguments = json.loads(tool_call.function.arguments)
                        prior = "<code>"
                        after = "</code>"
                        processed_messages.append(
                            f'\n{prior}    Tool Call: "{tool_call.function.name}"; Arguments: {arguments}"; Returned: {tool_content}{after}\n'
                        )
                        toolCallsResults.append({
                            "toolCallName": tool_call.function.name,
                            "toolCallArguments": arguments,
                            "toolCallResponse": tool_content
                        })

        elif isinstance(message, dict) and message['role'] == 'user':
            processed_messages.append(f"\nUser:\n{message['content']}")

    return "\n".join(processed_messages), toolCallsResults


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


def pretty_print_conversation(messages):
    """
    Used for printing the conversation history to the development console in readable and styled formatting

    Parameters
    ----------
    messages : list
    JSON-style message history of GPT conversation as a List of dictionary or ChatCompletionMessage objects
    """
    print("\n............................................ Message History ............................................")

    for message in messages:
        if isinstance(message, ChatCompletionMessage):
            print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Assistant:')
            if (message.content != None):
                print(str(message.content) + '\n')
        elif message["role"] == "system":
            print("\n" + Style.BRIGHT + Fore.YELLOW + 'System:')
            print(message['content'] + '\n')
        elif message["role"] == "user":
            print(Style.BRIGHT + Fore.LIGHTWHITE_EX + 'User:')
            print(message['content'] + '\n')
        elif message["role"] == "tool":
            print("    " + Style.BRIGHT + Fore.GREEN + "function" + message['name'] + ":")
            print("    " + message['content'])
