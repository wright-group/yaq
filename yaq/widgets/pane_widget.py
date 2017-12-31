"""Parent class for tab panes."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtWidgets

from .graph import Graph
from .push_button import PushButton
from .scroll_area import ScrollArea


# --- class ---------------------------------------------------------------------------------------


class PaneWidget(QtWidgets.QWidget):

    def __init__(self, main, graph=True, table=False, scroll=True):
        self.main = main
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        if graph:
            self.graph = Graph()
            layout.addWidget(self.graph)
        if scroll:
            self.scroll_area = ScrollArea()
            layout.addWidget(self.scroll_area)
        if table:
            # TODO:
            pass
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.add_widgets()
    
    def add_widgets(self):
        pass