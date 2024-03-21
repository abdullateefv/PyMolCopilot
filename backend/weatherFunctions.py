"""
Stores functions for retrieving weather data for function-calling use by GPT
(Just for demo purposes)
"""

import json


def get_current_weather(location, unit="fahrenheit"):
    """
    Retrieves weather data for a given location and returns it as a JSON formatted str

    Parameters
    ----------
    location: str
        Desired weather location
    unit : str
        Desired unit of temperature measurement

    Returns
    -------
    weather_data : str
        Weather data as a JSON formatted string
    """
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})

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
