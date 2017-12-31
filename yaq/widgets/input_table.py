"""Input table."""


# --- import --------------------------------------------------------------------------------------


from qtpy import QtWidgets


# --- class ---------------------------------------------------------------------------------------


class InputTable(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setColumnMinimumWidth(0, 150)
        self.layout().setColumnMinimumWidth(1, 150)
        self.layout().setMargin(0)

    def heading(self, name, global_object):
        raise NotImplementedError
        # heading
        heading = QtGui.QLabel(name)
        StyleSheet = 'QLabel{color: custom_color; font: bold 14px;}'.replace('custom_color', colors['heading_0'])
        heading.setStyleSheet(StyleSheet)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.layout().addWidget(heading, self.row_number, 0)
        self.controls.append(None)
        self.row_number += 1

    def number(self, name, global_object):
        raise NotImplementedError
        # heading
        heading = QtGui.QLabel(name)
        StyleSheet = 'QLabel{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
        heading.setStyleSheet(StyleSheet)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        self.layout().addWidget(heading, self.row_number, 0)
        #layout
        container_widget = QtGui.QWidget()
        container_widget.setLayout(QtGui.QHBoxLayout())
        layout = container_widget.layout()
        layout.setMargin(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        #control
        control = QtGui.QDoubleSpinBox()
        if global_object.display:
            control.setDisabled(True)
            StyleSheet = 'QDoubleSpinBox{color: custom_color_1; font: bold font_sizepx; border: 0px solid #000000;}'.replace('custom_color_1', g.colors_dict.read()['text_light']).replace('font_size', str(int(14)))
            StyleSheet += 'QScrollArea, QWidget{background: custom_color;  border-color: black;}'.replace('custom_color', g.colors_dict.read()['background'])                
        else:
            StyleSheet = 'QDoubleSpinBox{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
            StyleSheet += 'QScrollArea, QWidget{color: custom_color_1; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QWidget:disabled{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])                
        control.setStyleSheet(StyleSheet) 
        control.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        global_object.give_control(control)
        layout.addWidget(control)
        #units combobox
        if not global_object.units_kind == None:
            control.setMinimumWidth(self.width_input - 55)
            control.setMaximumWidth(self.width_input - 55)
            units = QtGui.QComboBox()
            units.setMinimumWidth(50)
            units.setMaximumWidth(50)
            StyleSheet = 'QComboBox{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QComboBox:disabled{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QAbstractItemView{color: custom_color_1; font: 50px solid white;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])       
            units.setStyleSheet(StyleSheet)
            layout.addWidget(units)
            global_object.give_units_combo(units)
        #finish
        self.layout().addWidget(container_widget, self.row_number, 1)
        self.controls.append(container_widget)
        self.row_number += 1

    def string(self, name, global_object):
        raise NotImplementedError
        #heading
        heading = QtGui.QLabel(name)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        StyleSheet = 'QLabel{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
        heading.setStyleSheet(StyleSheet)
        self.layout().addWidget(heading, self.row_number, 0)
        #control
        control = QtGui.QLineEdit()
        control.setMinimumWidth(self.width_input)
        control.setMaximumWidth(self.width_input)
        if global_object.display:
            control.setDisabled(True)
            StyleSheet = 'QWidget{color: custom_color_1; font: bold 14px; border: 0px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
        else:
            StyleSheet = 'QWidget{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QWidget:disabled{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])
        control.setStyleSheet(StyleSheet)
        global_object.give_control(control)
        #finish
        self.layout().addWidget(control, self.row_number, 1)
        self.controls.append(control)
        self.row_number += 1

    def combo(self, name, global_object):
        raise NotImplementedError
        #heading
        heading = QtGui.QLabel(name)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        StyleSheet = 'QLabel{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
        heading.setStyleSheet(StyleSheet)
        self.layout().addWidget(heading, self.row_number, 0)
        #control
        control = QtGui.QComboBox()
        control.setMinimumWidth(self.width_input)
        control.setMaximumWidth(self.width_input)
        if global_object.display:
            control.setDisabled(True)
            StyleSheet = 'QComboBox{color: custom_color_1; font: bold 14px; border: 0px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
            #StyleSheet += 'QComboBox:disabled{color: custom_color_1; font: 14px; border: 0px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QAbstractItemView{color: custom_color_1; font: 50px solid white; border: 0px white}'.replace('custom_color_1', colors['widget_background']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QComboBox::drop-down{border: 0;}'
        else:         
            StyleSheet = 'QComboBox{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QComboBox:disabled{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])
            StyleSheet += 'QAbstractItemView{color: custom_color_1; font: 50px solid white;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])       
        control.setStyleSheet(StyleSheet)
        global_object.give_control(control) 
        #finish
        self.layout().addWidget(control, self.row_number, 1)
        self.controls.append(control)
        self.row_number += 1

    def checkbox(self, name, global_object):
        raise NotImplementedError
        #heading
        heading = QtGui.QLabel(name)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        StyleSheet = 'QLabel{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
        heading.setStyleSheet(StyleSheet)
        self.layout().addWidget(heading, self.row_number, 0)
        #control
        if global_object.display:
            control = Led()
        else:
            control = QtGui.QCheckBox()
        global_object.give_control(control)
        #finish
        self.layout().addWidget(control, self.row_number, 1)
        self.controls.append(control)
        self.row_number += 1

    def filepath(self, name, global_object):
        raise NotImplementedError
        #heading
        heading = QtGui.QLabel(name)
        heading.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        StyleSheet = 'QLabel{color: custom_color; font: 14px;}'.replace('custom_color', colors['text_light'])
        heading.setStyleSheet(StyleSheet)
        self.layout().addWidget(heading, self.row_number, 0)
        #layout
        container_widget = QtGui.QWidget()
        container_widget.setLayout(QtGui.QHBoxLayout())
        layout = container_widget.layout()
        layout.setMargin(0)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        #push button
        load_button = QtGui.QPushButton('Load')
        StyleSheet = 'QPushButton{background:custom_color; border-width:0px;  border-radius: 0px; font: bold 14px}'.replace('custom_color', colors['go'])
        load_button.setStyleSheet(StyleSheet)
        load_button.setMinimumHeight(20)
        load_button.setMaximumHeight(20)
        load_button.setMinimumWidth(40)
        load_button.setMaximumWidth(40)
        layout.addWidget(load_button)
        global_object.give_button(load_button)
        #display
        display = QtGui.QLineEdit()
        #display.setDisabled(True)
        display.setReadOnly(True)
        display.setMinimumWidth(self.width_input - 45)
        display.setMaximumWidth(self.width_input - 45)
        StyleSheet = 'QWidget{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_light']).replace('custom_color_2', colors['widget_background'])
        StyleSheet += 'QWidget:disabled{color: custom_color_1; font: 14px; border: 1px solid custom_color_2; border-radius: 1px;}'.replace('custom_color_1', colors['text_disabled']).replace('custom_color_2', colors['widget_background'])
        display.setStyleSheet(StyleSheet)
        layout.addWidget(display)
        global_object.give_control(display)
        #finish
        self.layout().addWidget(container_widget, self.row_number, 1)
        self.controls.append(container_widget)
        self.row_number += 1
