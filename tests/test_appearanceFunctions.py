"""
Mocks prompts targeting BE functions in appearanceFunctions.py, tests for correct function call & success
"""


def test_bgColor_cmd(tool_call_validator):
    prompt = "Set the background color to blue."
    expected_function_name = "bgColor_cmd"
    expected_arguments = {'color': 'blue'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_refresh_cmd(tool_call_validator):
    prompt = "Refresh the screen."
    expected_function_name = "refresh_cmd"
    expected_arguments = {}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_cartoon_cmd(tool_call_validator):
    prompt = "Set the cartoon style to tube for the 'all' selection"
    expected_function_name = "cartoon_cmd"
    expected_arguments = {'type': 'tube', 'selection': 'all'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_color_cmd(tool_call_validator):
    prompt = "Set the color of selection to yellow"
    expected_function_name = "color_cmd"
    expected_arguments = {'color': 'yellow'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_fetch_cmd(tool_call_validator):
    prompt = "Download the file with code '1abc' and save it as 'my_file.pdb' in the background."
    expected_function_name = "fetch_cmd"
    expected_arguments = {'code': '1abc', 'path': 'my_file.pdb', 'async_': 1}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_deselect_cmd(tool_call_validator):
    prompt = "Disable all current selections."
    expected_function_name = "deselect_cmd"
    expected_arguments = {}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_id_atom_cmd(tool_call_validator):
    prompt = "Return the original source ID of atom 'CA' in chain A."
    expected_function_name = "id_atom_cmd"
    expected_arguments = {'selection': "chain A and name CA"}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)
