"""Progress bar."""

# --- import --------------------------------------------------------------------------------------


import os

from qtpy import QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class ProgressBar(QtWidgets.QProgressBar):
    
    def __init__(self):
        super().__init__()
        self.setFixedHeight(30)
        self.setMinimumWidth(600)
        self.setTextVisible(False)
