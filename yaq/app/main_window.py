"""yaq main window."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtGui, QtWidgets


# --- class ---------------------------------------------------------------------------------------


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app

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
    main_window.show()
    main_window.create_central_widget()
    app.exec_()


if __name__ == '__main__':
    main()
