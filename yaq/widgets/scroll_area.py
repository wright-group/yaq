"""Scroll area."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtCore, QtWidgets


# --- class ---------------------------------------------------------------------------------------


class ScrollArea(QtWidgets.QScrollArea):

    def __init__(self, show_bar=True):
        super().__init__()
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setFixedWidth(300)
        self.setWidgetResizable(True)
        if show_bar:
            self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.child = QtWidgets.QWidget()
        self.child.setLayout(QtWidgets.QVBoxLayout())
        self.child.layout().addStretch(1)
        self.setWidget(self.child)

    def add_widget(self, widget):
        self.child.layout().insertWidget(self.child.layout().count() - 1, widget)
        
        