"""yaq main window."""


# --- import -------------------------------------------------------------------------------------


from qtpy import QtGui, QtWidgets


# --- class --------------------------------------------------------------------------------------


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        print('hello world this is yaq MainWindow.__init__')

    def create_central_widget(self):
        print('hello world this is yaq MainWindow.create_main_frame')
        self.central_widget = QtWidgets.QWidget()
        hbox = QtWidgets.QHBoxLayout()
        # testing --------------------------------------------------------------------------------
        testing_box = QtWidgets.QVBoxLayout()
        widget = QtWidgets.QLabel('this is a qlabel on top of yaq')
        testing_box.addWidget(widget)
        hbox.addLayout(testing_box)
        # finish ---------------------------------------------------------------------------------
        self.central_widget.setLayout(hbox)
        self.setCentralWidget(self.central_widget)


# --- main ---------------------------------------------------------------------------------------


def main():
    """Initialize application and main window."""
    app = QtWidgets.QApplication(['yaq'])
    main_window = MainWindow(app)
    main_window.show()
    main_window.create_central_widget()
    app.exec_()


if __name__ == '__main__':
    main()
