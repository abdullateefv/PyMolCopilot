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
    
def refresh():
    """
    Redraws the scene as soon as the operating system allows it

    Returns
    -------
    results : str
        result of command execution as JSON formatted string
    """
    from pymol import cmd

    try:
        cmd.refresh()
        return json.dumps({"status": "success", "message": "Scene refreshed"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": "Unable to refresh scene"})