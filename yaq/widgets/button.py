"""Buttons."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtWidgets


class ShutDown(QtWidgets.QPushButton):

    def __init__(self):
        super().__init__()
        self.clicked.connect(self.initiate_shutdown)
        self.setText('SHUT DOWN')

    def initiate_shutdown(self):
        self.setText('SHUTTING DOWN')
        self.shutdown_go.emit()
