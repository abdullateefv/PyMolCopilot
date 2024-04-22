"""
Mocks prompts targeting BE functions in settingsFunctions.py, tests for correct function call & success
"""


def test_button_cmd(tool_call_validator):
    prompt = "Redefine the left Ctrl button to MovZ"
    expected_function_name = "button_cmd"
    expected_arguments = {'button': 'left', 'modifier': 'Ctrl', 'action': 'MovZ'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)
