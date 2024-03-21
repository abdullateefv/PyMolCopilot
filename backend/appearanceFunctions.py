"""
Stores functions for manipulating the appearance of PyMol elements
"""

import json


def bg_color(color):
    """
    Sets the background color

    Parameters
    ----------
    color: str
        Desired background color

    Returns
    -------
    results : str
        result of command execution as JSON formatted string
    """

    from pymol import cmd

    try:
        cmd.bg_color(color)
        return json.dumps({"status": "success", "bg_color_set": color})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed"})

from pymol import cmd

def attach_cmd(element, geometry, valence):
    """
    Adds a single atom onto the picked atom

    Parameters
    ----------
    element : str
        The chemical element of the atom, e.g. 'H' for hydrogen
    geometry : str
        The geometry of the atom, e.g. 1
    valence : int
        The valence of the atom, e.g. 1

    Returns
    -------
    results : str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.attach(element, geometry, valence)
        return json.dumps({"status": "success", "message": "Atom attached successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": "Failed to attach atom"})

    
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

cmd.extend("backward", backward_cmd)


import json
from pymol import cmd

def button_cmd(button, modifier, action):
    """
    Redefines what the mouse buttons do in PyMOL.

    Parameters
    ----------
    button : str
        The mouse button to redefine (e.g., left, middle, right, wheel, double_left, etc.).
    modifier : str
        The modifier key associated with the button (e.g., None, Shft, Ctrl, CtSh, etc.).
    action : str
        The action to be performed when the button is clicked (e.g., Rota, Move, MovZ, etc.).

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
    """
    try:
        cmd.button(button, modifier, action)
        return json.dumps({"status": "success", "message": "Button redefined successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": f"Failed to redefine button: {str(e)}"})
