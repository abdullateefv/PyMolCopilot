"""
Sets up pytest for project
"""


import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import pytest
from utilities.runConversation import run_conversation, process_messages

@pytest.fixture
def run_conversation_fixture():
    """
    Mocks prompt execution
    """
    def _run(newMessage, verbose=False):
        messages = run_conversation(newMessage, verbose)
        _, toolCallsResults = process_messages(messages, verbose)
        return toolCallsResults
    return _run


@pytest.fixture
def tool_call_validator(run_conversation_fixture):
    """
    Validates response with expectations
    """
    def _validator(prompt, expected_function_name, expected_arguments, expected_success):
        toolCallsResults = run_conversation_fixture(prompt)

        # Check if any tool calls were made
        assert len(toolCallsResults) > 0, "No tool calls made"

        # Initialize validation flags
        is_correct_function = False
        has_correct_arguments = False
        executed_successfully = False

        for toolCallResult in toolCallsResults:
            is_correct_function = toolCallResult["toolCallName"] == expected_function_name
            has_correct_arguments = toolCallResult["toolCallArguments"] == expected_arguments
            executed_successfully = toolCallResult["toolCallResponse"].get('success') == expected_success
            error_test =  toolCallResult["toolCallResponse"].get('success') 
            print(error_test)
            # If all conditions are met, validation passed, no need to check further
            if is_correct_function and has_correct_arguments and executed_successfully:
                break

        # Assertions are evaluated based on the final state of the flags
        assert is_correct_function, f"Incorrect function invoked: expected {expected_function_name}, got {toolCallResult['toolCallName']}"
        assert has_correct_arguments, f"Incorrect args passed: expected {expected_arguments}, got {toolCallResult['toolCallArguments']}"
        assert executed_successfully, "Function returned unsuccessfully"

    return _validator


