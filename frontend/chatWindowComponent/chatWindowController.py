"""
Loads chatWindowComponent UI and controls its logic
"""

from __future__ import absolute_import, print_function
import os
import sys

# Imports utilities module appropriately
plugin_dir = os.path.dirname(__file__)
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)
from utilities.runConversation import run_conversation


def make_dialog():
    """
    Loads the UI and manages UI logic
    """
    from pymol.Qt import QtWidgets
    from pymol.Qt.utils import loadUi

    # Load UI and stylesheet
    dialog = QtWidgets.QDialog()
    uifile = os.path.join(os.path.dirname(__file__), 'chatWindowView.ui')
    with open(os.path.join(os.path.dirname(__file__), 'chatWindowStyle.qss'), 'r') as stylesheet_file:
        dialog.setStyleSheet(stylesheet_file.read())

    form = loadUi(uifile, dialog)

    # Get UI Component References
    entryField, conversationField, sendButton = form.entryField, form.conversationField, form.sendButton

    # Send Button
    def onSend():
        """
        Called when the send button is clicked. Retrieves entered prompt from entryField and executes a conversation
        with GPT using run_conversation. Then appends the conversation messages to the UI.
        """
        enteredText = entryField.toPlainText()
        processed_messages = run_conversation(enteredText, True)
        conversationField.append(processed_messages)

    # Handle Send Button Click
    sendButton.clicked.connect(onSend)

    return dialog
