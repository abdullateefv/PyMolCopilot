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

    from pymol import cmd

    try:
        cmd.protect(selection)
        return json.dumps({"status": "success", "protected_atoms": selection, "message": "Given selection is protected."})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": "Given selection not identifiable. Unable to protect selection."})