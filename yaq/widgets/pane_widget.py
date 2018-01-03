"""Parent class for tab panes."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtWidgets

from .graph import Graph
from .push_button import PushButton
from .scroll_area import ScrollArea
from .table_widget import TableWidget


# --- class ---------------------------------------------------------------------------------------


class PaneWidget(QtWidgets.QWidget):

    def __init__(self, main, *, graph=True, table=False, scroll=True):
        self.main = main
        super().__init__()
        layout = QtWidgets.QHBoxLayout()
        if graph:
            self.graph = Graph()
            layout.addWidget(self.graph)
        if table:
            self.table = TableWidget()
            layout.addWidget(self.table)
        if scroll:
            self.scroll_area = ScrollArea()
            layout.addWidget(self.scroll_area)
        # TODO: add stretch if no graph or table
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.add_widgets()
    
    def add_widgets(self):
        pass