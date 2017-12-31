"""Push button."""

# --- import --------------------------------------------------------------------------------------


import collections
import os

from qtpy import QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class PushButton(QtWidgets.QPushButton):
    
    def __init__(self, label='', background='yellow'):
        super().__init__(label)
        self.setFixedHeight(30)
        # geometry
        style_sheet = 'QPushButton{border-width:0px; border-radius:0px}'
        style_sheet += 'QPushButton{font: bold}'
        # color
        style_sheet += 'QPushButton{background: %s}' % colors[background]
        self.setStyleSheet(style_sheet)
