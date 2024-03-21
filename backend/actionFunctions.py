import json

def bond(atom1, atom2): 
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
