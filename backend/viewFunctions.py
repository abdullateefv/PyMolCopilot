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


def quit_cmd():
    """
    Terminates the program.
    Parameters
    ----------
    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.quit()
        return json.dumps({"status": "success", "message": "Program terminated"})
    except Exception as errorMessage:
        return json.dumps({"status": "failed", "message": str(errorMessage)})
    
def index_cmd(selection='all'):
    """
    Returns a list of tuples corresponding to the object name and index of the atoms in the selection.
    The default value of string selection is all.

    Parameters
    ----------
    selection: str, optional (default is 'all')
        The name of the selection for which to get the index

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        index_list = cmd.index(selection)
        return json.dumps({"success": True, 'index_list': index_list})
    except Exception as errorMessage:
        return json.dumps({"success": False, 'message': str(errorMessage)})
    
def move_cmd(axis, distance):
    """
    Translates the camera about one of the three primary axes.

    Parameters
    ----------
    axis: str
        The axis along which to move the camera ('x', 'y', or 'z')
    distance: float
        The distance by which to move the camera along the specified axis

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.move(axis, distance)
        return json.dumps({"success": True, "message": f"Camera moved along {axis} axis by {distance}"})
    except Exception as errorMessage:
        return json.dumps({"success": False, "message": str(errorMessage)})

def orient_cmd(selection="all", state=0, animate=0.0):
    """
    Aligns the principal components of the atoms in the selection with the XYZ axes.

    Parameters
    ----------
    selection: str, optional (default is "all")
        The name of the selection or object that should be oriented
    state: int, optional (default is 0)
        The state of the object
    animate: float, optional (default is 0.0)
        Animation duration in seconds

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.orient(selection, state, animate)
        return json.dumps({"success": True, "message": "Orient function successfully called"})
    except Exception as errorMessage:
        return json.dumps({"success": False, "message": str(errorMessage)})