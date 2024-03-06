"""
Initializes plugin and loads chatWindow
"""

from __future__ import absolute_import
from __future__ import print_function
import os
import sys


# Imports frontend module appropriately
plugin_dir = os.path.dirname(__file__)
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)
from frontend.chatWindowComponent.chatWindowController import make_dialog

dialog = None

def __init_plugin__(app=None):
    """
    Initialize the plugin in PyMOL with the plugin name PyMol Copilot
    """
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('PyMol Copilot', run_plugin_gui)

def run_plugin_gui():
    """
    Open our custom dialog
    """
    global dialog
    if dialog is None:
        dialog = make_dialog()
    dialog.show()
