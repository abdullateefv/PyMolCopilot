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


def remove_cmd(selection):
    """
    creates a bond between two selections.

    Parameters
    ----------
    selection: str

    Returns
    -------
    The molecule without the selection. (since the selection will be removed.)

    """

    from pymol import cmd

    try:
        cmd.remove(selection)
        return json.dumps({"success": True, "messsage": "The selection has successfully removed"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": exceptionMessage})


def delete_cmd(name):
    """
    Removes objects and named selections.

    Parameters
    ----------
    name: str
        Name(s) of object(s) or selection(s), supports wildcards (*)

    Returns
    -------
    response: str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.delete(name)
        return json.dumps({"success": True, "message": "Specified selection successfully deleted"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": exceptionMessage})


def center_cmd(selection="all", state="0", origin="1"):
    """
    Translates the window and the origin to a point centered within the atom selection.

    Parameters
    ----------
    selection: str
        An singular atom or a chain that is meant to serve as the guidline to center
    state: int
        coordinate to match states.
    origin: int
        to move or not to move the center of the selection when centering.
    """

    from pymol import cmd

    try:
        cmd.center(selection, state, origin)
        return json.dumps({"success": True, "message": "Selection has been centered"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})


def h_fill_cmd():
    """
    Removes and replaces hydrogens on the atom or bond picked for editing.

    Returns
    -------
    results : str
        result of command execution as JSON formatted string
    """
    try:
        cmd.h_fill()
        return json.dumps({"status": "success", "message": "Successfully executed h_fill"})
    except Exception as exceptionMessage:
        return json.dumps({"status": "failed", "message": str(exceptionMessage)})
    
def indicate_cmd(selection="all"):
    """
    Shows a visual representation of an atom selection

    Parameters
    ----------
    selection : str, optional (Default is "all")
        The atom selection to indicate.

    Returns
    -------
    results : str
        Result of command execution as JSON formatted string
    """
    try:
        cmd.indicate(selection)
        return json.dumps({"success": True, "message": "Atom selection indicated"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})

def load_cmd(filename, object=None, state=0, format=None, finish=None, discrete=None,
            quiet=None, multiplex=None, zoom=None, partial=None, mimic=None, object_props=None,
            atom_props=None):
    """
    Load a file into PyMOL.

    Parameters
    ----------
    filename : str
        File path or URL.
    object_name : str, optional
        Name of the object (default: filename prefix).
    state : int, optional
        Number of the state into which the content should be loaded, or 0 for append (default: 0).
    file_format : str, optional
        Format of the data file (default: use file extension).
    finish : int, optional
        Finish parameter (default: None).
    discrete : int, optional
        Discrete parameter (default: None).
    quiet : int, optional
        Quiet parameter (default: None).
    multiplex : int, optional
        Multiplex parameter (default: None).
    zoom : int, optional
        Zoom parameter (default: None).
    partial : int, optional
        Partial parameter (default: None).
    mimic : int, optional
        Mimic parameter (default: None).
    object_props : str, optional
        Specifies whether properties should be loaded into PyMOL (default: use load_object_props_default setting).
    atom_props : str, optional
        Specifies whether atom properties should be loaded into PyMOL (default: use load_atom_props_default setting).

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
    """
    try:
        cmd.load(filename, object, state, format)
        return json.dumps({"success": True, "message": "File loaded successfully"})
    except Exception as exceptionMessage:
        return json.dumps({"success": False, "message": str(exceptionMessage)})