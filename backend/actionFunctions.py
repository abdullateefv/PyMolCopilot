import json

def bond(atom1, atom2): 
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
        cmd.bond(atom1, atom2)
        return json.dumps({"status": "success", "message": "Atoms are bonded"})
    except Exception as e:
        return json.dumps({"status": "failed", "message": "Unable to execute the bond command"})