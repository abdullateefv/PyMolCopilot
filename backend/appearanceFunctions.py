"""
Stores functions for manipulating the appearance of PyMol elements
"""

import json
from pymol import cmd


def bg_color(color):
    """
    Sets the background color

    Parameters
    ----------
    color: str
        Desired background color

    Returns
    -------
    response : str
        result of command execution as JSON formatted string
    """

    try:
        cmd.bg_color(color)
        return json.dumps({"status": "success", "bg_color_set": color})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed"})


def cartoon_cmd(type, selection=None):
    """
    Sets the cartoon display style

    Parameters
    ----------
    type: str
        The desired cartoon style
    selection: str
        Specifies the name of the selection that should have its cartoon style set

    Returns
    -------
    response : str
        result of command execution as JSON formatted string
    """
    try:
        if selection:
            cmd.cartoon(type, selection)
            return json.dumps({"status": "success", "type_set": type, "selection_set": selection})
        else:
            cmd.cartoon(type)
            return json.dumps({"status": "success", "type_set": type})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})
