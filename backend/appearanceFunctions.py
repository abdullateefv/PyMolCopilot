"""
Stores functions for manipulating the appearance of PyMol elements
Note: Only aesthetic functions
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

def refresh_cmd():
    """
    Redraws the scene as soon as the operating system allows it

    Returns
    -------
    results : str
        result of command execution as JSON formatted string
    """
    try:
        cmd.refresh()
        return json.dumps({"status": "success", "message": "Scene refreshed"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})

def color_cmd(color, selection="(all)"):
    """
    Changes the color of objects or atoms.

    Parameters
    ----------
    color : str
        Color name or number.
    selection : str, optional Default is "(all)"
        Selection expression or name pattern corresponding to the atoms or objects to be colored.

    Returns
    -------
    results : str
        Result of command execution as JSON formatted string.
    """

    from pymol import cmd

    try:
        if cmd.get_color_index(color) == -1:
                raise ValueError("Invalid color name")
        cmd.color(color, selection)
        return json.dumps({"status": "success", "color_set": color, "selection": selection})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})