import json
import os
import sys
from importlib import import_module


def test_function_consistency():
    # Adjust the path to the 'toolsDescription.json' as needed
    json_file_path = os.path.join(os.path.dirname(__file__), '..', 'backend', 'toolsDescription.json')

    # Count functions in toolsDescription.json
    with open(json_file_path, 'r') as file:
        tools = json.load(file)
        json_function_count = len(tools)

    # Count functions in Python files in the backend directory
    backend_function_count = 0
    backend_dir = os.path.join(os.path.dirname(__file__), '..', 'backend')
    for filename in os.listdir(backend_dir):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]  # remove '.py'
            module_path = f"backend.{module_name}"
            module = import_module(module_path)
            backend_function_count += len(
                [func for func in dir(module) if callable(getattr(module, func)) and not func.startswith("__")])

    # Import available_functions dynamically
    sys_path_append = os.path.join(os.path.dirname(__file__), '..')
    if sys_path_append not in sys.path:
        sys.path.append(sys_path_append)
    from utilities.runConversation import available_functions
    available_function_count = len(available_functions)

    # Count test functions in other test files
    test_dir = os.path.dirname(__file__)
    test_function_count = 0
    for file in os.listdir(test_dir):
        if file.startswith('test_') and file not in ['test_general.py', 'conftest.py']:
            with open(os.path.join(test_dir, file), 'r') as test_file:
                test_function_count += sum(1 for line in test_file if line.strip().startswith('def test_'))

    if json_function_count == backend_function_count == test_function_count == available_function_count:
        print(
            f"\033[1;32m Tools Description Function Count: {json_function_count} | Implemented Function Count: {backend_function_count} | Function Test Count: {test_function_count} | Available Function Count: {available_function_count}\033[0m")
    else:
        print(
            f"\033[1;31m Tools Description Function Count: {json_function_count} | Implemented Function Count: {backend_function_count} | Function Test Count: {test_function_count} | Available Function Count: {available_function_count}\033[0m")

    # Assert all counts are equal
    assert json_function_count == backend_function_count, f"Mismatch between # of functions described in toolsDescription and # of backend functions implemented: {json_function_count} vs {backend_function_count}"
    assert json_function_count == available_function_count, f"Mismatch between # of functions described in toolsDescription and # of functions imported in runConversation: {json_function_count} vs {available_function_count}"
    assert test_function_count == json_function_count, f"Mismatch between # of function tests written and # of functions described in toolsDescription: {test_function_count} vs {json_function_count}"
