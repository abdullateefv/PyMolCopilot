"""
Stores functions for manipulating the appearance of PyMol elements
"""

import json
from pymol import cmd

def bgColor_cmd(color=None, rgb=None):
    """
    Sets the background color

    Parameters
    ----------
    color: str, optional (default is None)
        Desired background color
    rgb: list, optional (default is None)
        RGB decimal format

    Returns
    -------
    response : str
        result of command execution as JSON formatted string
    """
    try:
        if color is not None:
            if cmd.get_color_index(color) == -1:
                raise ValueError("Invalid color name, consider using a custom RGB color list instead")
            cmd.bg_color(color)
        elif rgb is not None:
            cmd.set_color("custom_color", rgb)
            cmd.bg_color("custom_color")
        else:
            raise ValueError("Must enter either a color name or a RGB value")

        return json.dumps({"status": "success", "bg_color_set": color if color else "custom_color"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})


def cartoon_cmd(type, selection=None):
    """
    Sets the cartoon display style

    Parameters
    ----------
    type: str
        The desired cartoon style
    selection: str, optional (default is None)
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
    
def protect(selection):
    """
    Protects a set of atoms from transformations

    Parameters
    ----------
    selection: str
        Selection of atoms to protect

    Returns
    -------
    results : str
        Result of command execution as JSON formatted string
    """

    try:
        cmd.protect(selection)
        return json.dumps({"status": "success", "protected_atoms": selection, "message": "Given selection is protected."})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})
