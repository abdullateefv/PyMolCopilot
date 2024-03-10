from enum import Enum
import json

class Color(Enum):
    RED = (1.0, 0.0, 0.0)
    GREEN = (0.0, 1.0, 0.0)
    BLUE = (0.0, 0.0, 1.0)
    YELLOW = (1.0, 1.0, 0.0)
    WHITE = (1.0, 1.0, 1.0)

def bg_color(color=None, rgb=None):
    """
    Sets the background color

    Parameters
    ----------
    color: str, optional
        Desired background color (default is None)
    rgb: tuple, optional
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
                raise ValueError("Invalid color name")
            cmd.bg_color(color)
        elif rgb is not None:
            cmd.set_color("custom_color", rgb)
            cmd.bg_color("custom_color")
        else:
            raise ValueError("Both color name and RGB value are None")

        return json.dumps({"status": "success", "bg_color_set": color if color else "custom_color"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed"})
