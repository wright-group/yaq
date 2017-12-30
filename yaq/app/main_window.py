"""yaq main window."""


# --- import --------------------------------------------------------------------------------------


import appdirs
import ctypes
import os
import sys

import qtpy
from qtpy import QtGui, QtWidgets

from ..__version__ import __version__


# --- define --------------------------------------------------------------------------------------


here = os.path.abspath(os.path.basename(__file__))


# --- class ---------------------------------------------------------------------------------------


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.__version__ = __version__
        # title
        title = 'yaq : yet another acquisition'
        title += ' | version %s' % self.__version__
        title += ' | Python %i.%i' % (sys.version_info[0], sys.version_info[1])
        title += ' | %s' % qtpy.API
        self.setWindowTitle(title)
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
        # TODO: finish
        screen = QtGui.QDesktopWidget().screenGeometry() 
        size = self.geometry() 
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def create_central_widget(self):
        self.central_widget = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        # queue button ----------------------------------------------------------------------------
        queue_button = QtWidgets.QPushButton('QUEUE')
        queue_button.setFixedHeight(30)
        queue_button.setFixedWidth(300)
        queue_button.clicked.connect(self.on_queue_clicked)
        layout.addWidget(queue_button, 0, 0)
        # progress bar ----------------------------------------------------------------------------
        progress_bar = QtWidgets.QProgressBar()
        progress_bar.setFixedHeight(30)
        layout.addWidget(progress_bar, 0, 1)
        # hardware scroll area --------------------------------------------------------------------
        # TODO
        # queue scroll area -----------------------------------------------------------------------
        # TODO
        # tabs ------------------------------------------------------------------------------------
        self.tabs = QtWidgets.QTabWidget()
        layout.addWidget(self.tabs, 1, 1)
        # finish ----------------------------------------------------------------------------------
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

    def on_shutdown_clicked(self):
        print('on shutdown clicked')

    def on_queue_clicked(self):
        print('on queue clicked')


# --- main ----------------------------------------------------------------------------------------


def main():
    """Initialize application and main window."""
    app = QtWidgets.QApplication(['yaq'])
    main_window = MainWindow(app)
    main_window.create_central_widget()
    main_window.showMaximized()
    app.exec_()


if __name__ == '__main__':
    main()
