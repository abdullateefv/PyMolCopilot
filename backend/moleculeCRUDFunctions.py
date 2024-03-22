"""
This file contains any functions that perform the CRUD operations on functions
"""

import json
from pymol import cmd

def create_cmd(name, selection):
    """
    Creates a new molecule object from a selection.  It can also be used to update an existing object to the selection.

    Parameters
    ----------
    name: str
        name of object to create or modify
    selection: str
        The name of the selection that will be included in the new object

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.create(name, selection)
        return json.dumps({"status": "success", "name_set": name, "selection_used": selection})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "error": exceptionMessage})

def bond_cmd(atom1, atom2):
    """
   creates a bond between two selections

    Parameters
    ----------
    atom1: str
       The first atom selection
    atom2: str
       The second atom selection

    Returns
    -------
    bonded atom structure
    """

    from pymol import cmd

    try:
        cmd.bond(atom1, atom2)
        return json.dumps({"status": "success", "message": "Atoms are bonded"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})
