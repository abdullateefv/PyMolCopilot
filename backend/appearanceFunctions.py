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
    Changes the color of objects or atoms.
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

def fetch_cmd(code, name=None, state=None, type='', async_=1, path=None):
    """
    Downloads a file '13AN' from the internet (if possible).

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
            
        return json.dumps({ "success" : True, "message": "File fetched successfully"})
    except Exception as e:
        return json.dumps({"success" : False, "message": f"Failed to fetch file: {str(e)}"})


# #---trial
# import json
# from pymol import cmd







# def fetch_cmd(code, name=None, state=None, type="", async_=0, path=None):
#     """
#     Downloads a file from the internet (if possible).

#     Parameters
#     ----------
#     code : str
#         A single PDB identifier or a list of identifiers. Supports 5-letter codes for fetching single chains (e.g., "1a00A").
#     name : str, optional
#         The object name into which the file should be loaded.
#     state : int, optional
#         The state number into which the file should be loaded.
#     type : str, optional
#         The file type to fetch. Options include cif, pdb, pdb1, 2fofc, fofc, emd, cid, sid. Default is "cif".
#     async_ : int, optional
#         Whether to download in the background and not block the PyMOL command line. Default is 0.
#     path : str, optional
#         The path to save the downloaded file.

#     Returns
#     -------
#     results : str
#         Result of command execution as JSON-formatted string.
        
#     """
    
#     try:
#         # cmd.async_ = async_  # Update async_ parameter
#         if (name==None and state==None and path==None):
#             cmd.fetch(code=code, type=type, async_=async_)
#         elif(name==None and path==None):
#             cmd.fetch(code=code, state=state, type=type, async_=async_)
#         elif(name==None and state==None):
#             cmd.fetch(code=code, type=type, async_=async_, path=path)
#         elif(state==None and path==None):
#             cmd.fetch(code=code, name=name, type=type, async_=async_)
#         elif(name==None):
#             cmd.fetch(code=code, state=state, type=type, async_=async_, path=path)
#         elif(state==None):
#             cmd.fetch(code=code, name=name, type=type, async_=async_, path=path)
#         elif(path==None):
#             cmd.fetch(code=code, name=name, state=state, type=type, async_=async_)
#         else:
#             cmd.fetch(code=code, name=name, state= state, type=type, async_=async_, path=path)
            
#         return json.dumps({"status": "success", "message": "File fetched successfully"})
#     except Exception as e:
#         return json.dumps({"status": "failed", "message": f"Failed to fetch file: {str(e)}"})



import json
from pymol import cmd

# def deselect_cmd():
#     """
#     Disables any and all visible selections.

#     Returns
#     -------
#     str
#         JSON-formatted string indicating the status of the operation.
#     """
#     try:
#         cmd.deselect()
#         return json.dumps({"status": "success", "message": "Selections deselected successfully"})
#     except Exception as e:
#         return json.dumps({"status": "failed", "message": f"Failed to deselect selections: {str(e)}"})


#------ ORIGINAL
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
        return json.dumps({"success" : True, "message": "Selections deselected successfully"})
    except Exception as e:
        return json.dumps({"success" : False, "message": f"Failed to deselect selections: {str(e)}"})

deselect_cmd()

import json
from pymol import cmd

# def id_atom_cmd(selection):
#     """
#     Returns the original source ID of a single atom.

#     Parameters
#     ----------
#     selection : str
#         Atom selection in PyMOL.

#     Returns
#     -------
#     int
#         Original source ID of the atom.

#     Raises
#     ------
#     ValueError
#         If the atom does not exist or if the selection corresponds to multiple atoms.
#     """
#     try:
#         atom_id = cmd.id_atom(selection)
#         return json.dumps({"status": "success", "atom_id": atom_id})
#     except Exception as e:
#         return json.dumps({"status": "failed", "message": f"Failed to retrieve atom ID: {str(e)}"})
#         return json.dumps({"success": False, "message": str(exceptionMessage)})




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
        return json.dumps({"success" : True, "atom_id": atom_id})
    except Exception as e:
        return json.dumps({"success" : False, "message": f"Failed to retrieve atom ID: {str(e)}"})



