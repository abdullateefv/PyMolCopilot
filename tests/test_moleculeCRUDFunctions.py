"""
Mocks prompts targeting BE functions in moleculeCRUDFunctions.py, tests for correct function call & success
"""


def test_create_cmd(tool_call_validator):
    prompt = "Create a new molecule called newMol from the 'all' selection"
    expected_function_name = "create_cmd"
    expected_arguments = {'name': 'newMol', 'selection': 'all'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_bond_cmd(tool_call_validator):
    prompt = "Create a bond between the all and all atom selections"
    expected_function_name = "bond_cmd"
    expected_arguments = {'atom1': 'all', 'atom2': 'all'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_protect_cmd(tool_call_validator):
    prompt = "Protect the all selection"
    expected_function_name = "protect_cmd"
    expected_arguments = {'selection': 'all'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


def test_attach_cmd(tool_call_validator):
    prompt = "Attach a hydrogen with geometry 1 and valence 1"
    expected_function_name = "attach_cmd"
    expected_arguments = {'element': 'H', 'geometry': 1, 'valence': 1}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)