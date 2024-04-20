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
        return json.dumps({"success": True, "name_set": name, "selection_used": selection})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "error": str(exceptionMessage)})


def bond_cmd(atom1, atom2):
    """
    Creates a bond between two selections

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
        return json.dumps({"success": True, "message": "Selections have been bonded"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": exceptionMessage})


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
        return json.dumps(
            {"success": True, "protected_atoms": selection, "message": "Given selection has been protected"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})


def attach_cmd(element, geometry, valence):
    """
    Adds a single atom onto the picked atom

    Parameters
    ----------
    element : str
        The chemical element of the atom, e.g. 'H' for hydrogen
    geometry : int
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
        return json.dumps({"success": True, "message": "Atom attached successfully"})
    except Exception as e:
        return json.dumps({"success": False, "message": "Failed to attach atom"})


def pop_cmd(name, source):
    """
    Provides a mechanism of iterating through an atom selection
    atom by atom, where each atom is sequentially assigned to the
    named selection.

    Parameters
    ----------
    name : str
        Name of the destination selection.
    source : str
        Name of the source selection.

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
    """
    try:
        cmd.pop(name,source)
        return json.dumps({"success": True, "message": "Pop command executed successfully"})
    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})
    
    
def identify_cmd(selection=("all"), mode=0):
    """
    Returns a list of atom IDs corresponding to the ID code
    of atoms in the selection.
    noteee: this is actual parameter selection="(all)"cle, mode=0
    Parameters
    ----------
    selection : str, optional
        Atom selection. Default is "(all)".
    mode : int, optional
        Identification mode. 0: return a list of identifiers, 1: return a list of tuples of the object name and the identifier.
        Default is 0.

    Returns
    -------
    results : list
        List of atom IDs or tuples of object name and atom ID based on the mode.
    """
    try:
        identifiers = cmd.identify(selection, mode)
        if mode == 1:
            # Convert identifiers to list of tuples of object name and identifier
            results = [(obj, atom_id) for obj, atom_id in identifiers]
        else:
            # Return list of identifiers
            results = identifiers
        return json.dumps({"success": True, "identifiers": results})
    except Exception as e:
        return json.dumps({"success": False, "message": str(e)})

