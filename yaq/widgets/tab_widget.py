"""Tab widget."""


# --- import --------------------------------------------------------------------------------------


import collections
import logging
import os

from qtpy import QtWidgets

from ..core.ini import INI


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']

log = logging.getLogger(__name__)


# --- class ---------------------------------------------------------------------------------------


class TabWidget(QtWidgets.QTabWidget):

    def __init__(self):
        super().__init__()
        self.widgets = collections.OrderedDict()
        # geometry
        style_sheet = 'QTabBar::tab{width: 130px; height: 30px; border: 0px; font: bold}'
        style_sheet += 'QTabBar::tab:!selected{margin-top: 0px}'
        style_sheet += 'QTabWidget::pane{border-top: 2px solid %s;}' % colors['selection']    
        # colors
        style_sheet += 'QTabBar::tab{background-color: %s}' % colors['background']
        style_sheet += 'QTabBar::tab:selected{color: %s}' % colors['yellow']
        style_sheet += 'QTabBar::tab:!selected{color: %s}' % colors['foreground']
        self.setStyleSheet(style_sheet)
        log.debug('TabWidget initialized')
        
    def add_tab(self, name):
        widget = QtWidgets.QWidget()
        layout = QtWidgets.QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 0)
        widget.setLayout(layout)
        self.addTab(widget, name)
        self.widgets[name] = widget
