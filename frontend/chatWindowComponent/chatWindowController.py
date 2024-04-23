from __future__ import absolute_import, print_function
import os
import sys
from pymol.Qt import QtCore

# Imports utilities module appropriately
plugin_dir = os.path.dirname(__file__)
if plugin_dir not in sys.path:
    sys.path.insert(0, plugin_dir)
from utilities.runConversation import run_conversation, process_messages, style_messages


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

    entryField.setPlaceholderText("Message PyMol Assistant...")

    # Send Button
    def onSend():
        """
        Called when the send button is clicked. Retrieves entered prompt from entryField and executes a conversation
        with GPT using run_conversation. Then appends the processed & formatted conversation messages to the UI.
        """
        newPrompt = entryField.toPlainText()

        messages = run_conversation(newPrompt)
        processedMessages, _ = process_messages(messages)
        HTMLStyledMessages = style_messages(processedMessages)
        print(HTMLStyledMessages)
        conversationField.append(HTMLStyledMessages)

        # Clear the text entry field
        entryField.clear()

    # Handle Send Button Click
    sendButton.clicked.connect(onSend)

    # Handle Enter Key Press
    def onEnterPress(event):
        """
        Called when the Enter key is pressed in the entryField. Sends the message and clears the text entry field.
        """
        if event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter:
            onSend()
            entryField.clear()
        else:

            # Allow normal typing

            QtWidgets.QTextEdit.keyPressEvent(entryField, event)

    entryField.keyPressEvent = onEnterPress

    return dialog