import maya.cmds as cmds

from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui


class ChairGenerator():

    def __init__(self):
        self.seat_width = 2.0
        self.seat_depth = 2.0
        self.seat_thickness = 0.2

        self.leg_height = 2.0
        self.back_leg_height = 3.8
        self.leg_width = 0.2

        self.apron_height = 0.19
        self.apron_thickness = 0.15
        self.apron_vertical_position = 0.0

        self.cushion_width = 1.8
        self.cushion_depth = 1.8
        self.cushion_thickness = 0.15

        self.backrest_width = 1.6
        self.backrest_height = 1.2
        self.backrest_thickness = 0.15

        self.is_bed = False

        self.grp_name = "chair_GRP"

    def create(self):

        group_objs = []

        self.create_seat()
        group_objs.append(self.seat_obj)

        self.create_legs()
        group_objs.append(self.leg1)
        group_objs.append(self.leg2)
        group_objs.append(self.leg3)
        group_objs.append(self.leg4)

        self.create_seat_apron()
        group_objs.append(self.apron1)
        group_objs.append(self.apron2)
        group_objs.append(self.apron3)
        group_objs.append(self.apron4)

        self.create_seat_cushion()
        group_objs.append(self.cushion_obj)

        self.create_backrest()
        group_objs.append(self.backrest_obj)

        self.chair_grp = cmds.group(
            group_objs,
            name=self.grp_name
        )

        cmds.setAttr(
            f"{self.chair_grp}.translateY",
            2.0
        )

    def create_seat(self):
        self.seat_obj, self.seat_node = cmds.polyCube(
            name="seat",
            width=self.seat_width,
            height=self.seat_thickness,
            depth=self.seat_depth
        )

        return self.seat_obj

    def create_legs(self):

        self.leg1, self.leg1_node = cmds.polyCube(
            name="front_left_leg",
            width=self.leg_width,
            height=self.leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg1}.translateY",
            -self.leg_height / 2.0
        )

        cmds.setAttr(
            f"{self.leg1}.translateX",
            -self.seat_width / 2.0 + self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.leg1}.translateZ",
            self.seat_depth / 2.0 - self.leg_width / 2.0
        )

        self.leg2, self.leg2_node = cmds.polyCube(
            name="front_right_leg",
            width=self.leg_width,
            height=self.leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg2}.translateY",
            -self.leg_height / 2.0
        )

        cmds.setAttr(
            f"{self.leg2}.translateX",
            self.seat_width / 2.0 - self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.leg2}.translateZ",
            self.seat_depth / 2.0 - self.leg_width / 2.0
        )

        self.leg3, self.leg3_node = cmds.polyCube(
            name="back_left_leg_backrest_support",
            width=self.leg_width,
            height=self.back_leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg3}.translateY",
            -self.leg_height + self.back_leg_height / 2.0
        )

        cmds.setAttr(
            f"{self.leg3}.translateX",
            -self.seat_width / 2.0 + self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.leg3}.translateZ",
            -self.seat_depth / 2.0 + self.leg_width / 2.0
        )

        self.leg4, self.leg4_node = cmds.polyCube(
            name="back_right_leg_backrest_support",
            width=self.leg_width,
            height=self.back_leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg4}.translateY",
            -self.leg_height + self.back_leg_height / 2.0
        )

        cmds.setAttr(
            f"{self.leg4}.translateX",
            self.seat_width / 2.0 - self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.leg4}.translateZ",
            -self.seat_depth / 2.0 + self.leg_width / 2.0
        )

    def create_seat_apron(self):

        self.apron1, self.apron1_node = cmds.polyCube(
            name="front_apron",
            width=self.seat_width - self.leg_width * 2,
            height=self.apron_height,
            depth=self.apron_thickness
        )

        cmds.setAttr(
            f"{self.apron1}.translateY",
            -self.seat_thickness / 2.0
            - self.apron_height / 2.0
            - self.apron_vertical_position
        )

        cmds.setAttr(
            f"{self.apron1}.translateZ",
            self.seat_depth / 2.0 - self.apron_thickness / 2.0 - 0.02
        )

        self.apron2, self.apron2_node = cmds.polyCube(
            name="back_apron",
            width=self.seat_width - self.leg_width * 2,
            height=self.apron_height,
            depth=self.apron_thickness
        )

        cmds.setAttr(
            f"{self.apron2}.translateY",
            -self.seat_thickness / 2.0
            - self.apron_height / 2.0
            - self.apron_vertical_position
        )

        cmds.setAttr(
            f"{self.apron2}.translateZ",
            -self.seat_depth / 2.0 + self.apron_thickness / 2.0 + 0.02
        )

        self.apron3, self.apron3_node = cmds.polyCube(
            name="left_apron",
            width=self.apron_thickness,
            height=self.apron_height,
            depth=self.seat_depth - self.leg_width * 2
        )

        cmds.setAttr(
            f"{self.apron3}.translateY",
            -self.seat_thickness / 2.0
            - self.apron_height / 2.0
            - self.apron_vertical_position
        )

        cmds.setAttr(
            f"{self.apron3}.translateX",
            -self.seat_width / 2.0 + self.apron_thickness / 2.0 + 0.02
        )

        self.apron4, self.apron4_node = cmds.polyCube(
            name="right_apron",
            width=self.apron_thickness,
            height=self.apron_height,
            depth=self.seat_depth - self.leg_width * 2
        )

        cmds.setAttr(
            f"{self.apron4}.translateY",
            -self.seat_thickness / 2.0
            - self.apron_height / 2.0
            - self.apron_vertical_position
        )

        cmds.setAttr(
            f"{self.apron4}.translateX",
            self.seat_width / 2.0 - self.apron_thickness / 2.0 - 0.02
        )

    def create_seat_cushion(self):

        self.cushion_obj, self.cushion_node = cmds.polyCube(
            name="seat_cushion",
            width=self.cushion_width,
            height=self.cushion_thickness,
            depth=self.cushion_depth
        )

        cmds.setAttr(
            f"{self.cushion_obj}.translateY",
            0.175
        )

        cmds.setAttr(
            f"{self.cushion_obj}.translateZ",
            0.098
        )

        cmds.setAttr(
            f"{self.cushion_obj}.scaleZ",
            0.966
        )

    def create_backrest(self):

        self.backrest_obj, self.backrest_node = cmds.polyCube(
            name="backrest",
            width=self.backrest_width,
            height=self.backrest_height,
            depth=self.backrest_thickness
        )

        cmds.setAttr(
            f"{self.backrest_obj}.translateX",
            0
        )

        cmds.setAttr(
            f"{self.backrest_obj}.translateY",
            1.317
        )

        cmds.setAttr(
            f"{self.backrest_obj}.translateZ",
            -self.seat_depth / 2.0 + self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.backrest_obj}.scaleY",
            0.712
        )


def get_main_maya_win():
    main_win = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_win), QtWidgets.QWidget)


class ChairGeneratorGUI(QtWidgets.QDialog):

    def __init__(self):
        super().__init__(parent=get_main_maya_win())

        self.chair_generator = ChairGenerator()

        self.setWindowTitle("Chair Generator")
        self.setWindowFlag(QtCore.Qt.WindowType.Tool)

        self.create_layout()
        self.create_connections()

    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()

        self.form_lay = QtWidgets.QFormLayout()

        self.enablepreset_cb = QtWidgets.QCheckBox()
        self.enablepreset_cb.setChecked(False)

        self.form_lay.addRow(
            "Enable Chair Presets",
            self.enablepreset_cb
        )

        self.preset_cb = QtWidgets.QComboBox()

        self.preset_cb.addItems([
            "Floating Apron Chair",
            "Wide Chair (Bench Style)",
            "Lounge Chair",
            "Bed (Extra Option)"
        ])

        self.preset_cb.setEnabled(False)

        self.form_lay.addRow(
            "Chair Preset",
            self.preset_cb
        )

        self.seat_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_width_dspnbx.setValue(2.0)

        self.form_lay.addRow(
            "Seat Width",
            self.seat_width_dspnbx
        )

        self.seat_depth_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_depth_dspnbx.setValue(2.0)

        self.form_lay.addRow(
            "Seat Depth",
            self.seat_depth_dspnbx
        )

        self.seat_thickness_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_thickness_dspnbx.setValue(0.2)

        self.form_lay.addRow(
            "Seat Thickness",
            self.seat_thickness_dspnbx
        )

        self.leg_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.leg_width_dspnbx.setValue(0.2)

        self.form_lay.addRow(
            "Leg Width",
            self.leg_width_dspnbx
        )

        self.cushion_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_width_dspnbx.setValue(1.8)

        self.form_lay.addRow(
            "Cushion Width",
            self.cushion_width_dspnbx
        )

        self.cushion_depth_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_depth_dspnbx.setValue(1.8)

        self.form_lay.addRow(
            "Cushion Depth",
            self.cushion_depth_dspnbx
        )

        self.cushion_height_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_height_dspnbx.setValue(0.15)

        self.form_lay.addRow(
            "Cushion Height",
            self.cushion_height_dspnbx
        )

        self.backrest_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.backrest_width_dspnbx.setValue(1.6)

        self.form_lay.addRow(
            "Backrest Width",
            self.backrest_width_dspnbx
        )

        self.backrest_height_dspnbx = QtWidgets.QDoubleSpinBox()
        self.backrest_height_dspnbx.setValue(1.2)

        self.form_lay.addRow(
            "Backrest Height",
            self.backrest_height_dspnbx
        )

        self.apron_vertical_position_dspnbx = QtWidgets.QDoubleSpinBox()
        self.apron_vertical_position_dspnbx.setRange(-1.5, 1.5)
        self.apron_vertical_position_dspnbx.setSingleStep(0.1)
        self.apron_vertical_position_dspnbx.setValue(0.0)

        self.form_lay.addRow(
            "Apron Vertical Position",
            self.apron_vertical_position_dspnbx
        )

        self.enablegrpname_cb = QtWidgets.QCheckBox()
        self.enablegrpname_cb.setChecked(False)

        self.form_lay.addRow(
            "Enable Group Name",
            self.enablegrpname_cb
        )

        self.grpname_le = QtWidgets.QLineEdit()
        self.grpname_le.setText(self.chair_generator.grp_name)
        self.grpname_le.setEnabled(False)

        self.form_lay.addRow(
            "Group Name",
            self.grpname_le
        )

        self.main_lay.addLayout(self.form_lay)

        self.create_btn = QtWidgets.QPushButton("Create")

        self.reset_btn = QtWidgets.QPushButton("Reset")

        self.button_lay = QtWidgets.QHBoxLayout()

        self.button_lay.addWidget(self.create_btn)
        self.button_lay.addWidget(self.reset_btn)

        self.main_lay.addLayout(self.button_lay)

        self.setLayout(self.main_lay)

    def create_connections(self):
        self.enablepreset_cb.toggled.connect(self.toggle_presets)
        self.preset_cb.currentTextChanged.connect(self.apply_chair_preset)

        self.enablegrpname_cb.toggled.connect(self.toggle_grpname_le)

        self.create_btn.clicked.connect(self.create)
        self.reset_btn.clicked.connect(self.reset_parameters)

    @QtCore.Slot(bool)
    def toggle_presets(self, enabled):

        self.preset_cb.setEnabled(enabled)

        if enabled:
            self.apply_chair_preset(self.preset_cb.currentText())

        else:
            self.restore_original_parameters()

    @QtCore.Slot(bool)
    def toggle_grpname_le(self, enabled):

        self.grpname_le.setEnabled(enabled)

        if not enabled:
            self.grpname_le.setText("chair_GRP")

    def restore_original_parameters(self):

        self.chair_generator = ChairGenerator()

        self.seat_width_dspnbx.setValue(2.0)
        self.seat_depth_dspnbx.setValue(2.0)
        self.seat_thickness_dspnbx.setValue(0.2)

        self.leg_width_dspnbx.setValue(0.2)

        self.cushion_width_dspnbx.setValue(1.8)
        self.cushion_depth_dspnbx.setValue(1.8)
        self.cushion_height_dspnbx.setValue(0.15)

        self.backrest_width_dspnbx.setValue(1.6)
        self.backrest_height_dspnbx.setValue(1.2)

        self.apron_vertical_position_dspnbx.setValue(0.0)

    @QtCore.Slot(str)
    def apply_chair_preset(self, preset_name):

        if not self.enablepreset_cb.isChecked():
            return

        self.chair_generator.is_bed = False

        if preset_name == "Floating Apron Chair":

            self.restore_original_parameters()

            self.apron_vertical_position_dspnbx.setValue(0.65)

        elif preset_name == "Wide Chair (Bench Style)":

            self.seat_width_dspnbx.setValue(4.5)
            self.seat_depth_dspnbx.setValue(2.0)
            self.seat_thickness_dspnbx.setValue(0.2)

            self.leg_width_dspnbx.setValue(0.25)

            self.cushion_width_dspnbx.setValue(4.3)
            self.cushion_depth_dspnbx.setValue(1.8)
            self.cushion_height_dspnbx.setValue(0.18)

            self.backrest_width_dspnbx.setValue(4.1)
            self.backrest_height_dspnbx.setValue(1.2)

            self.apron_vertical_position_dspnbx.setValue(0.0)

        elif preset_name == "Lounge Chair":

            self.seat_width_dspnbx.setValue(2.4)
            self.seat_depth_dspnbx.setValue(2.8)
            self.seat_thickness_dspnbx.setValue(0.2)

            self.leg_width_dspnbx.setValue(0.2)

            self.cushion_width_dspnbx.setValue(2.2)
            self.cushion_depth_dspnbx.setValue(2.6)
            self.cushion_height_dspnbx.setValue(0.25)

            self.backrest_width_dspnbx.setValue(2.0)
            self.backrest_height_dspnbx.setValue(1.5)

            self.apron_vertical_position_dspnbx.setValue(0.0)

        elif preset_name == "Bed (Extra Option)":

            self.chair_generator.is_bed = True

            self.seat_width_dspnbx.setValue(3.5)
            self.seat_depth_dspnbx.setValue(6.0)
            self.seat_thickness_dspnbx.setValue(0.25)

            self.leg_width_dspnbx.setValue(0.3)

            self.cushion_width_dspnbx.setValue(3.3)
            self.cushion_depth_dspnbx.setValue(5.8)
            self.cushion_height_dspnbx.setValue(0.3)

            self.backrest_width_dspnbx.setValue(2.9)
            self.backrest_height_dspnbx.setValue(0.7)

            self.apron_vertical_position_dspnbx.setValue(0.0)

    @QtCore.Slot()
    def reset_parameters(self):

        self.enablepreset_cb.setChecked(False)

        self.preset_cb.setCurrentIndex(0)

        self.preset_cb.setEnabled(False)

        self.restore_original_parameters()

        self.enablegrpname_cb.setChecked(False)

        self.grpname_le.setText("chair_GRP")
        self.grpname_le.setEnabled(False)

    @QtCore.Slot()
    def create(self):

        self.chair_generator.seat_width = self.seat_width_dspnbx.value()
        self.chair_generator.seat_depth = self.seat_depth_dspnbx.value()

        self.chair_generator.seat_thickness = (
            self.seat_thickness_dspnbx.value()
        )

        self.chair_generator.leg_width = self.leg_width_dspnbx.value()

        self.chair_generator.cushion_width = self.cushion_width_dspnbx.value()
        self.chair_generator.cushion_depth = self.cushion_depth_dspnbx.value()

        self.chair_generator.cushion_thickness = (
            self.cushion_height_dspnbx.value()
        )

        self.chair_generator.backrest_width = (
            self.backrest_width_dspnbx.value()
        )

        self.chair_generator.backrest_height = (
            self.backrest_height_dspnbx.value()
        )

        if self.chair_generator.is_bed:

            self.chair_generator.backrest_width = (
                self.chair_generator.seat_width
                - self.chair_generator.leg_width * 2
            )

            self.backrest_width_dspnbx.setValue(
                self.chair_generator.backrest_width
            )

        self.chair_generator.apron_vertical_position = (
            self.apron_vertical_position_dspnbx.value()
        )

        self.chair_generator.grp_name = self.grpname_le.text()

        self.chair_generator.create()
