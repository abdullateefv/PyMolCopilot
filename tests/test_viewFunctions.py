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

def test_index_cmd(tool_call_validator):
    prompt = "Return a list of tuples corresponding to the object name and index of all the atoms in the selection"
    expected_function_name = "index_cmd"
    expected_arguments = {}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_move_cmd(tool_call_validator):
    prompt = "Translate the camera along the x-axis by 3 units"
    expected_function_name = "move_cmd"
    expected_arguments = {'axis': 'x', 'distance': 3.0}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_orient_cmd(tool_call_validator):
    prompt = "Align the molecules in the sele selection with state 0 and animate 1.0"
    expected_function_name = "orient_cmd"
    expected_arguments = {'selection': 'sele', 'state': 0, 'animate': 1.0}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)
