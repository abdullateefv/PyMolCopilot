"""
Mocks prompts for each backend function, tests for correct function call & success
"""


def test_bgColor_cmd(tool_call_validator):
    prompt = "Set the background color to blue."
    expected_function_name = "bgColor_cmd"
    expected_arguments = {'color': 'blue'}
    expected_success = True

    # Now the fixture itself handles the assertions
    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_refresh_cmd(tool_call_validator):
    prompt = "Refresh the screen."
    expected_function_name = "refresh_cmd"
    expected_arguments = {}
    expected_success = True

    # The fixture handles the assertions
    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_cartoon_cmd(tool_call_validator):
    prompt = "Set the cartoon style to tube for the sele selection"
    expected_function_name = "refresh_cmd"
    expected_arguments = {'type': 'tube', 'selection': 'sele'}
    expected_success = True

    # The fixture handles the assertions
    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)
