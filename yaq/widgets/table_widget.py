"""Table widget."""


# --- import --------------------------------------------------------------------------------------


import os

from qtpy import QtCore, QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']


# --- class ---------------------------------------------------------------------------------------


class TableWidget(QtWidgets.QTableWidget):

    def __init__(self):
        super().__init__()
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        # geometry
        style_sheet = 'QTableWidget::item{padding: 2px}'
        style_sheet +=  'QHeaderView::section{border: 0px}'
        style_sheet += 'QTableView{border: 0px; gridline-color: %s}' % colors['selection']
        # color
        style_sheet += 'QTableWidget{background-color: %s;}' % colors['background']
        style_sheet += 'QHeaderView::section{background: %s;}' % colors['background']
        style_sheet +=  'QHeaderView::section{color: %s; font: bold}' % colors['foreground']
        style_sheet += 'QTableWidget::section{border: 5px solid red;}'# % colors['background']
        self.setStyleSheet(style_sheet)
        self.setGridStyle(QtCore.Qt.SolidLine)
        self.setShowGrid(True)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

    def set_columns(self, **kwargs):
        """name: width"""
        for i, w in enumerate(kwargs.values()):
            self.insertColumn(i)
            if w is None:
                self.horizontalHeader().setResizeMode(i, QtWidgets.QHeaderView.Stretch)
            else:
                self.setColumnWidth(i, w)
        self.setHorizontalHeaderLabels(kwargs.keys())
