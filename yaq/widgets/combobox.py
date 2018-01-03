"""ComboBox."""

# --- import --------------------------------------------------------------------------------------


import os

from qtpy import QtCore, QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class ComboBox(QtWidgets.QComboBox):
    
    def __init__(self):
        super().__init__()
