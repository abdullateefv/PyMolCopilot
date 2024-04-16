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


# def test_fetch_cmd(tool_call_validator):
#     prompt = "Downloads a file '1A3N' from the internet (if possible)."
#     expected_function_name = "fetch_cmd"
#     expected_arguments = {'code': '1A3N', 'name': None, 'state': None, 'type': '', 'async_': 0, 'path': None}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)



#------------------- FOR TRIAL --------------------
# def test_fetch_cmd(tool_call_validator):
#     prompt = "Download the file with code '1abc' and save it as 'my_file.pdb' in the background."
#     expected_function_name = "fetch_cmd"
#     # Update the expected arguments to reflect the correct behavior
#     expected_arguments = {'code': '1abc', 'path': 'my_file.pdb', 'async_': 1, 'type': ''}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

# def test_deselect_cmd(tool_call_validator):
#     prompt = "Disable all current selections."
#     expected_function_name = "deselect_cmd"
#     expected_arguments = {}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

# def test_id_atom_cmd(tool_call_validator):
#     prompt = "Return the original source ID of atom 'CA' in chain A."
#     expected_function_name = "id_atom_cmd"
#     expected_arguments = {'selection': "chain A and name CA"}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

# ===== TRIAL 2
# def test_fetch_cmd(tool_call_validator):
#     prompt = "Downloads a file '1A3N' from the internet (if possible)."
#     expected_function_name = "fetch_cmd"
#     expected_arguments = {'code': '1A3N', 'state': None,'async_': 1, 'path': None}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_fetch_cmd(tool_call_validator):
    prompt = "Download file '1A3N' with name as '1A3N' , state as '2', file type as 'cif', async set to '1', and path as '2'from Internet"
    expected_function_name = "fetch_cmd"
    expected_arguments = {'code': '1A3N', 'name': '1A3N', 'state': 2, 'type': 'cif', 'async_': 1, 'path': '2'}


    expected_success = True
    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)




# def test_deselect_cmd(tool_call_validator):
#     prompt = "Disable all current selections."
#     expected_function_name = "deselect_cmd"
#     expected_arguments = {}
#     # Update the assertion to check for successful function return
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)


# def test_id_atom_cmd(tool_call_validator):
#     prompt = "Return the original source ID of atom 'CA' in chain A."
#     expected_function_name = "id_atom_cmd"
#     expected_arguments = {'selection': "chain A and name CA"}
#     expected_success = True

#     tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)
# #     # Update the assertion to check for successful function return


from pymol import cmd
# ----- original
def test_deselect_cmd(tool_call_validator):
    prompt = "Disable all current selections."
    expected_function_name = "deselect_cmd"
    expected_arguments = {}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

def test_id_atom_cmd(tool_call_validator):
    cmd.fetch('6UGC')
    cmd.select("sele", "id 1") #creating sele
    cmd.select("sele", "first sele") #redefing sele to first_seles
    prompt = "give the id_atom of selected atom"
    expected_function_name = "id_atom_cmd"
    expected_arguments = {'selection': 'sele'}
    expected_success = True

    tool_call_validator(prompt, expected_function_name, expected_arguments, expected_success)

