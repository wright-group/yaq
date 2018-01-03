"""Parent class for tab panes."""


# --- import --------------------------------------------------------------------------------------


import logging

import WrightTools as wt

from .input_table import InputTable
from .label import Label
from .pane_widget import PaneWidget
from .push_button import PushButton


# --- import --------------------------------------------------------------------------------------


log = logging.getLogger(__name__)


# --- class ---------------------------------------------------------------------------------------


class LoggingWidget(PaneWidget, logging.Handler):
    
    def __init__(self, *args, **kwargs):
        kwargs['graph'] = False 
        kwargs['table'] = True
        kwargs['scroll'] = True
        PaneWidget.__init__(self, *args, **kwargs)
        logging.Handler.__init__(self)
        self.table.set_columns(TIMESTAMP=125, LEVEL=100, SOURCE=300, MESSAGE=None)
        self.register()
        log.debug('complete')
        
    def add_widgets(self):
        self.input_table = InputTable()
        self.scroll_area.add_widget(self.input_table)
        self.log_button = PushButton('PRODUCE LOG', 'green')
        self.log_button.clicked.connect(self.on_log_button_clicked)
        self.scroll_area.add_widget(self.log_button)
        
    def emit(self, record):
        row = self.table.rowCount()
        self.table.insertRow(row)
        # color
        if record.levelno < 10:  # NOTSET
            color = 'blue'
        elif 10 <= record.levelno < 20:  # DEBUG
            color = 'aqua'
        elif 20 <= record.levelno < 30:  # INFO
            color = 'foreground'
        elif 30 <= record.levelno < 40:  # WARNING
            color = 'yellow'
        elif 40 <= record.levelno < 50:  # ERROR
            color = 'orange'
        else:
            color = 'red'
        # timestamp
        ts = wt.kit.TimeStamp(at=record.created)
        self.table.setCellWidget(row, 0, Label(ts.human, alignment='center', color=color))
        # level
        self.table.setCellWidget(row, 1, Label(record.levelname, alignment='center', color=color))
        # source
        source = ':'.join([record.name, record.funcName])
        self.table.setCellWidget(row, 2, Label(source, alignment='center', color=color))
        # message
        self.table.setCellWidget(row, 3, Label(record.getMessage(), alignment='center', 
                                               color=color))
        # remove trailing
        if row >= 100:
            self.table.removeRow(row-100)
        self.table.scrollToBottom()

    def on_log_button_clicked(self):
        try:
            log.debug('log here')
            1/0
        except Exception as e:
            log.error(e)
    
    def register(self):
        """Register self to upstream logger."""
        yaq = logging.getLogger('yaq')
        yaq.addHandler(self)