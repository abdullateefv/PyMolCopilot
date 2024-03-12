"""
Stores functions for manipulating the appearance of PyMol elements
"""

import json

def bg_color(color=None, rgb=None):
    """
    Sets the background color

    Parameters
    ----------
    color: str, optional
        Desired background color (default is None)
    rgb: array, optional
        RGB decimal format (default is None)

    Returns
    -------
    results : str
        result of command execution as JSON formatted string
    """

    from pymol import cmd

    try:
        if color is not None:
            if cmd.get_color_index(color) == -1:
                raise ValueError("Invalid color name, consider using a custom RGB color array instead")
            cmd.bg_color(color)
        elif rgb is not None:
            cmd.set_color("custom_color", rgb)
            cmd.bg_color("custom_color")
        else:
            raise ValueError("Must enter either a color name or a RGB value")

        return json.dumps({"status": "success", "bg_color_set": color if color else "custom_color"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": "Given color not identifiable. Unable to change color."})
