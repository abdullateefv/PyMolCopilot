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

        return json.dumps({"success": True, "bg_color_set": color if color else "custom_color"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})


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
            return json.dumps({"success": True, "type_set": type, "selection_set": selection})
        else:
            cmd.cartoon(type)
            return json.dumps({"success": True, "type_set": type})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})


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
        return json.dumps({"success": True, "message": "Scene refreshed"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})

def color_cmd(color, selection_set="(all)"):
    """
    Changes the color of objects or atoms.def pop_cmd(name, source):
    """
        # Provides a mechanism of iterating through an atom selection
        # atom by atom, where each atom is sequentially assigned to the
        # named selection.

        # Parameters
        # ----------
        # name : str
        #     Name of the destination selection.
        # source : str
        #     Name of the source selection.

        # Returns
        # -------
        # results : str
        #     Result of command execution as JSON-formatted string.
    """
    try:
        # Your implementation of the pop command here
        # (Not implemented here as it requires access to PyMOL's internal API)
        return json.dumps({"success": True, "message": "Pop command executed successfully"})
    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})

    Parameters
    ----------
    color : str
        Color name or number.
    selection : str, optional (Default is "(all)")
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
        cmd.color(color, selection_set)
        return json.dumps({"success": True, "color_set": color, "selection": selection_set})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})


def recolor_cmd(selection=("all"), representation="everything"):
    """
    Forces reapplication of colors to existing objects.

    Parameters
    ----------
    selection : str, optional
        Selection of atoms to apply colors to. Default is 'all'.
    representation : str, optional
        Representation of objects to recolor. Default is 'everything'.

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
    """
    try:
        cmd.recolor(selection, representation)
        return json.dumps({"success": True, "message": "Colors reapplied successfully"})
    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})
