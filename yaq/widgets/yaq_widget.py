"""Create main yaq widget."""


# --- import --------------------------------------------------------------------------------------


from .main_widget import MainWidget
from .tab_widget import TabWidget


# --- class ---------------------------------------------------------------------------------------


class YAQWidget(TabWidget):

    def __init__(self, main, parent):
        self.main = main
        super().__init__()
        parent.layout().addWidget(self)
        self.setContentsMargins(0, 0, 0, 0)
        self.addTab(MainWidget(self.main), 'MAIN')
        self.addTab(MainWidget(self.main), 'MONITOR')
        self.add_tab('LOAD')
        self.add_tab('LOGGING')
        self.add_tab('BACKUP')
        self.add_tab('COMMUNICATION')
        
