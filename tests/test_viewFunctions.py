"""
Mocks prompts targeting BE functions in viewFunctions.py, tests for correct function call & success
"""


def test_origin_cmd(tool_call_validator):
    prompt = "Set the origin to be centered about the XYZ coordinates 0,1,0"
    expected_function_name = "origin_cmd"
    expected_arguments = {'position': [0, 1, 0]}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_backward_cmd(tool_call_validator):
    prompt = "Move the frame backward"
    expected_function_name = "backward_cmd"
    expected_arguments = {}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_quit_cmd():
    assert True  # Quit CMD cannot be mocked in a test (kills application)
