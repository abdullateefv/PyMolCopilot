"""
This file contains functions that affect the PyMOL View
Note: Not aesthetics or any CRUD operations
"""

import json
from pymol import cmd

def origin_cmd(selection=None, position=None):
    """
    Sets center of rotation. Defaults to the center of all objects if params None. Otherwise, set to about the named
    selection/object or specified position coordinates.

    Parameters
    ----------
    selection: str, optional (default is None)
        The name of the selection or object that should be set as the origin (center) of rotation
    position: list, optional (default is None)
        The XYZ coordinates that should be set as the origin (center) of rotation provided as a list of three numbers

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        if selection is not None:
            cmd.origin(selection)
            return json.dumps({'status': 'success', 'origin_set': selection})
        elif position is not None:
            cmd.origin(position=position)
            return json.dumps({'status': 'success', 'origin_set': position})
        else:
            cmd.origin()
            return json.dumps({'status': 'success', 'origin_set': '(all)'})
    except Exception as errorMessage:
        return json.dumps({'status': 'failed', 'message': errorMessage})

def backward_cmd():
    """
    Moves the movie back one frame.

    Args:
        None

    Returns:
        None
    """
    try:
        cmd.backward()
        return json.dumps({"status": "success", "message": "Backward function successfully called"})
    except:
        return json.dumps({"status": "failed", "message": "Unable to call backward"})

def quit_cmd(code=0):
    """
    Terminates the program.

    Parameters
    ----------
    code: int, optional (default is 0)
        The status code to exit the application with

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.quit(code)
        return json.dumps({"status": "success", "message": "Program terminated"})
    except Exception as errorMessage:
        return json.dumps({"status": "failed", "message": errorMessage})