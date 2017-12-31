"""Parent class for tab panes."""


# --- import --------------------------------------------------------------------------------------


from .pane_widget import PaneWidget
from .push_button import PushButton


# --- class ---------------------------------------------------------------------------------------


class MainWidget(PaneWidget):

    def add_widgets(self):
        self.shutdown_button = PushButton('SHUTDOWN YAQ', 'red')
        self.shutdown_button.clicked.connect(self.main.on_shutdown_clicked)
        self.scroll_area.add_widget(self.shutdown_button)
