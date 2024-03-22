"""
This file contains any functions related to manipulating or performing CRUD operations on objects/molecules
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
    try:
        cmd.bond(atom1, atom2)
        return json.dumps({"status": "success", "message": "Atoms are bonded"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": exceptionMessage})

def protect_cmd(selection):
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

def attach_cmd(element, geometry, valence):
    """
    Adds a single atom onto the picked atom

    Parameters
    ----------
    element : str
        The chemical element of the atom, e.g. 'H' for hydrogen
    geometry : str
        The geometry of the atom, e.g. 1
    valence : int
        The valence of the atom, e.g. 1

    Returns
    -------
    results : str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.attach(element, geometry, valence)
        return json.dumps({"status": "success", "message": "Atom attached successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": "Failed to attach atom"})
    
def center(selection=None, state=None, origin=None): 
    """

    """

    from pymol import cmd

    try: 
        cmd.center(selection, state, origin)
        return json.dumps({"status": "success", "message": "Selection has been centered"})
    except Exception as exceptionMessage: 
        return json.dumps({"status": "failed", "message": exceptionMessage})
