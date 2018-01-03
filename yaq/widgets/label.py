"""Label."""

# --- import --------------------------------------------------------------------------------------


import os

from qtpy import QtCore, QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class Label(QtWidgets.QLabel):
    
    def __init__(self, text, *, alignment='left', color='foreground'):
        super().__init__(text)
        StyleSheet = 'QLabel{color: %s;}' % colors[color]
        self.setStyleSheet(StyleSheet)
        if alignment == 'left':
            self.setAlignment(QtCore.Qt.AlignLeft)
        elif alignment == 'center':
            self.setAlignment(QtCore.Qt.AlignCenter)
        elif alignment == 'right':
            self.setAlignment(QtCore.Qt.AlignRight)
