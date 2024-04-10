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

from pymol import cmd

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

    
def backward_cmd():
    """
    Moves the movie back one frame.

    Args:
        None

    Returns:
        None
    """
    try:
        cmd.backward()
        return json.dumps({"status": "success", "message": "Backward function successfully called"})
    except:
        return json.dumps({"status": "failed", "message": "Unable to call backward"})


import json
from pymol import cmd

def button_cmd(button, modifier, action):
    """
    Redefines what the mouse buttons do in PyMOL.

    Parameters
    ----------
    button : str
        The mouse button to redefine (e.g., left, middle, right, wheel, double_left, etc.).
    modifier : str
        The modifier key associated with the button (e.g., None, Shft, Ctrl, CtSh, etc.).
    action : str
        The action to be performed when the button is clicked (e.g., Rota, Move, MovZ, etc.).

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
    """
    try:
        cmd.button(button, modifier, action)
        return json.dumps({"status": "success", "message": "Button redefined successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": f"Failed to redefine button: {str(e)}"})

import json
from pymol import cmd

def fetch_cmd(code, name=None, state=None, type="", async_=0, path=None):
    """
    Downloads a file from the internet (if possible).

    Parameters
    ----------
    code : str
        A single PDB identifier or a list of identifiers. Supports 5-letter codes for fetching single chains (e.g., "1a00A").
    name : str, optional
        The object name into which the file should be loaded.
    state : int, optional
        The state number into which the file should be loaded.
    type : str, optional
        The file type to fetch. Options include cif, pdb, pdb1, 2fofc, fofc, emd, cid, sid. Default is "cif".
    async_ : int, optional
        Whether to download in the background and not block the PyMOL command line. Default is 0.
    path : str, optional
        The path to save the downloaded file.

    Returns
    -------
    results : str
        Result of command execution as JSON-formatted string.
        
    """
    
    try:
        if (name==None and state==None and path==None):
            cmd.fetch(code=code, type=type, async_=async_)
        elif(name==None and path==None):
            cmd.fetch(code=code, state=state, type=type, async_=async_)
        elif(name==None and state==None):
            cmd.fetch(code=code, type=type, async_=async_, path=path)
        elif(state==None and path==None):
            cmd.fetch(code=code, name=name, type=type, async_=async_)
        elif(name==None):
            cmd.fetch(code=code, state=state, type=type, async_=async_, path=path)
        elif(state==None):
            cmd.fetch(code=code, name=name, type=type, async_=async_, path=path)
        elif(path==None):
            cmd.fetch(code=code, name=name, state=state, type=type, async_=async_)
        else:
            cmd.fetch(code=code, name=name, state= state, type=type, async_=async_, path=path)
            
        return json.dumps({"status": "success", "message": "File fetched successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": f"Failed to fetch file: {str(e)}"})



def deselect_cmd():
    """
    Disables any and all visible selections.

    Returns
    -------
    None
        No return value.
    """
    try:
        cmd.deselect()
        return json.dumps({"status": "success", "message": "Selections deselected successfully"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": f"Failed to deselect selections: {str(e)}"})

import json
from pymol import cmd

def id_atom_cmd(selection):
    """
    Returns the original source ID of a single atom.

    Parameters
    ----------
    selection : str
        Atom selection in PyMOL.

    Returns
    -------
    int
        Original source ID of the atom.

    Raises
    ------
    ValueError
        If the atom does not exist or if the selection corresponds to multiple atoms.
    """
    try:
        atom_id = cmd.id_atom(selection)
        return json.dumps({"status": "success", "atom_id": atom_id})
    except Exception as e:
        return json.dumps({"status": "failed", "message": f"Failed to retrieve atom ID: {str(e)}"})
