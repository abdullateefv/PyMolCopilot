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
            return json.dumps({"success": True, 'origin_set': selection})
        elif position is not None:
            cmd.origin(position=position)
            return json.dumps({"success": True, 'origin_set': position})
        else:
            cmd.origin()
            return json.dumps({"success": True, 'origin_set': '(all)'})
    except Exception as errorMessage:
        return json.dumps({"success": False, 'message': str(errorMessage)})

def backward_cmd():
    """
    Moves the movie back one frame

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.backward()
        return json.dumps({"success": True, "message": "Backward function successfully called"})
    except Exception as errorMessage:
        return json.dumps({"success": False, "message": str(errorMessage)})
