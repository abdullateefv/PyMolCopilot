"""
This file contains functions that modify editor settings
"""

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
        return json.dumps({"success": True, "message": "Button redefined successfully"})
    except Exception as e:
        return json.dumps({"success": False, "message": f"Failed to redefine button: {str(e)}"})
