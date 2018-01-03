"""yaq main window."""


# --- import --------------------------------------------------------------------------------------


import appdirs
import ctypes
import logging
import os
import sys

import WrightTools as wt

import qtpy
from qtpy import QtCore, QtGui, QtWidgets

from ..__version__ import __version__
from ..core.ini import INI
from .progress_bar import ProgressBar
from .push_button import PushButton
from .tab_widget import TabWidget
from .yaq_widget import YAQWidget


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.dirname(__file__))

colors = INI(os.path.join(here, 'colors.ini')).dictionary['night']

log = logging.getLogger(__name__)


# --- class ---------------------------------------------------------------------------------------


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.start_time = wt.kit.TimeStamp()
        self.app = app
        self.__version__ = __version__
        # title
        title = 'yaq : yet another acquisition'
        title += ' | version %s' % self.__version__
        title += ' | Python %i.%i' % (sys.version_info[0], sys.version_info[1])
        title += ' | %s' % qtpy.API
        self.setWindowTitle(title)
        # style sheet
        style_sheet = 'QWidget{background-color: %s}' % colors['background']
        self.setStyleSheet(style_sheet)
        # disable 'x'
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        # platform specific
        if os.name == 'posix':
            pass
        elif os.name == 'nt':
            # must have unique app ID
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('yaq')
            # icon
            p = os.path.join(appdirs.user_data_dir(), 'yaq', 'icon.ico')
            self.setWindowIcon(QtGui.QIcon(p))
        
    def center(self):
        """Center the window within the current screen."""
        raise NotImplementedError
        screen = QtGui.QDesktopWidget().screenGeometry() 
        size = self.geometry() 
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def create_central_widget(self):
        self.central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        # queue button
        queue_button = PushButton('RUN QUEUE', 'green')
        queue_button.setFixedWidth(300)
        queue_button.clicked.connect(self.on_queue_clicked)
        layout.addWidget(queue_button, 0, 0)
        # progress bar
        progress_bar = ProgressBar()
        layout.addWidget(progress_bar, 0, 1)
        # hardware scroll area
        # TODO
        # tabs
        self.tabs = TabWidget()
        self.tabs.add_tab('YAQ')
        self.tabs.add_tab('MOTOR')
        self.tabs.add_tab('SENSORY')
        self.tabs.add_tab('AUTONOMIC')
        self.tabs.add_tab('SOMATIC')
        layout.addWidget(self.tabs, 1, 1)
        # finish
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)
        
    def initialize_log(self):
        d = os.path.join(appdirs.user_data_dir(), 'yaq', 'logs')
        if not os.path.isdir(d):
            os.mkdir(d)
        p = os.path.join(d, self.start_time.path + '.log')
        elements = ['%(asctime)s',
                    '%(levelname)s',
                    '%(name)s',
                    '%(funcName)s',
                    '%(message)s']
        fmt = '|'.join(elements)
        logging.basicConfig(filename=p, level=logging.DEBUG, format=fmt)
        logging.captureWarnings(True)
        log.info('log initialized')
        
    def initialize_tab_widgets(self):
        YAQWidget(self, self.tabs.widgets['YAQ'])

    def on_shutdown_clicked(self):
        print('on shutdown clicked')
        log.info('attempting shutdown')
        self.close()

    def on_queue_clicked(self):
        print('on queue clicked')


# --- main ----------------------------------------------------------------------------------------


def main():
    """Initialize application and main window."""
    app = QtWidgets.QApplication(['yaq'])
    main_window = MainWindow(app)
    main_window.initialize_log()
    main_window.create_central_widget()
    main_window.showMaximized()
    main_window.initialize_tab_widgets()
    app.exec_()


if __name__ == '__main__':
    main()
