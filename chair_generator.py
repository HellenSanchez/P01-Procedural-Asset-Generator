import maya.cmds as cmds

from PySide6 import QtWidgets, QtCore
from shiboken6 import wrapInstance

import maya.OpenMayaUI as omui


class ChairGenerator():

    def __init__(self):
        # Seat parameters
        self.seat_width = 2.0
        self.seat_depth = 2.0
        self.seat_thickness = 0.2

        # Leg parameters
        self.leg_height = 2.0
        self.back_leg_height = 3.8
        self.leg_width = 0.2

        # Seat apron parameters
        self.apron_height = 0.3
        self.apron_thickness = 0.15

        # Seat cushion parameters
        self.cushion_width = 1.8
        self.cushion_depth = 1.8
        self.cushion_thickness = 0.15

        # Backrest parameters
        self.backrest_width = 1.6
        self.backrest_height = 1.2
        self.backrest_thickness = 0.15

        self.grp_name = "chair_GRP"

    # Main function to create the chair
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

    # Create seat
    def create_seat(self):
        self.seat_obj, self.seat_node = cmds.polyCube(
            name="seat",
            width=self.seat_width,
            height=self.seat_thickness,
            depth=self.seat_depth
        )

        return self.seat_obj

    # Create chair legs
    # Back legs extend upward to serve as backrest supports
    def create_legs(self):

        # Front left leg
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

        # Front right leg
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

        # Back left leg (also serves as a backrest support)
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

        # Back right leg (also serves as a backrest support)
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

    # Create wooden seat apron
    def create_seat_apron(self):

        # Front apron
        self.apron1, self.apron1_node = cmds.polyCube(
            name="front_apron",
            width=self.seat_width - self.leg_width * 2,
            height=self.apron_height,
            depth=self.apron_thickness
        )

        cmds.setAttr(
            f"{self.apron1}.translateY",
            -self.seat_thickness / 2.0 - self.apron_height / 2.0
        )

        cmds.setAttr(
            f"{self.apron1}.translateZ",
            self.seat_depth / 2.0 - self.apron_thickness / 2.0 - 0.02
        )

        # Back apron
        self.apron2, self.apron2_node = cmds.polyCube(
            name="back_apron",
            width=self.seat_width - self.leg_width * 2,
            height=self.apron_height,
            depth=self.apron_thickness
        )

        cmds.setAttr(
            f"{self.apron2}.translateY",
            -self.seat_thickness / 2.0 - self.apron_height / 2.0
        )

        cmds.setAttr(
            f"{self.apron2}.translateZ",
            -self.seat_depth / 2.0 + self.apron_thickness / 2.0 + 0.02
        )

        # Left apron
        self.apron3, self.apron3_node = cmds.polyCube(
            name="left_apron",
            width=self.apron_thickness,
            height=self.apron_height,
            depth=self.seat_depth - self.leg_width * 2
        )

        cmds.setAttr(
            f"{self.apron3}.translateY",
            -self.seat_thickness / 2.0 - self.apron_height / 2.0
        )

        cmds.setAttr(
            f"{self.apron3}.translateX",
            -self.seat_width / 2.0 + self.apron_thickness / 2.0 + 0.02
        )

        # Right apron
        self.apron4, self.apron4_node = cmds.polyCube(
            name="right_apron",
            width=self.apron_thickness,
            height=self.apron_height,
            depth=self.seat_depth - self.leg_width * 2
        )

        cmds.setAttr(
            f"{self.apron4}.translateY",
            -self.seat_thickness / 2.0 - self.apron_height / 2.0
        )

        cmds.setAttr(
            f"{self.apron4}.translateX",
            self.seat_width / 2.0 - self.apron_thickness / 2.0 - 0.02
        )

    # Create seat cushion
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

    # Create chair backrest
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
            -0.9
        )

        cmds.setAttr(
            f"{self.backrest_obj}.scaleY",
            0.712
        )


# Get Maya main window
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

    # Create main GUI layout
    def create_layout(self):
        self.main_lay = QtWidgets.QVBoxLayout()

        # Seat width parameter
        self.form_lay = QtWidgets.QFormLayout()

        self.seat_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_width_dspnbx.setValue(2.0)

        self.form_lay.addRow(
            "Seat Width",
            self.seat_width_dspnbx
        )

        # Seat depth parameter
        self.seat_depth_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_depth_dspnbx.setValue(2.0)

        self.form_lay.addRow(
            "Seat Depth",
            self.seat_depth_dspnbx
        )

        # Seat thickness parameter
        self.seat_thickness_dspnbx = QtWidgets.QDoubleSpinBox()
        self.seat_thickness_dspnbx.setValue(0.2)

        self.form_lay.addRow(
            "Seat Thickness",
            self.seat_thickness_dspnbx
        )

        # Leg width parameter
        self.leg_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.leg_width_dspnbx.setValue(0.2)

        self.form_lay.addRow(
            "Leg Width",
            self.leg_width_dspnbx
        )

        # Cushion width parameter
        self.cushion_width_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_width_dspnbx.setValue(1.8)

        self.form_lay.addRow(
            "Cushion Width",
            self.cushion_width_dspnbx
        )

        # Cushion depth parameter
        self.cushion_depth_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_depth_dspnbx.setValue(1.8)

        self.form_lay.addRow(
            "Cushion Depth",
            self.cushion_depth_dspnbx
        )

        # Cushion height parameter
        self.cushion_height_dspnbx = QtWidgets.QDoubleSpinBox()
        self.cushion_height_dspnbx.setValue(0.15)

        self.form_lay.addRow(
            "Cushion Height",
            self.cushion_height_dspnbx
        )

        self.main_lay.addLayout(self.form_lay)

        self.create_btn = QtWidgets.QPushButton("Create")

        self.main_lay.addWidget(self.create_btn)

        self.setLayout(self.main_lay)

    # Connect GUI buttons
    def create_connections(self):
        self.create_btn.clicked.connect(self.create)

    @QtCore.Slot()
    def create(self):

        self.chair_generator.seat_width = self.seat_width_dspnbx.value()
        self.chair_generator.seat_depth = self.seat_depth_dspnbx.value()
        self.chair_generator.seat_thickness = self.seat_thickness_dspnbx.value()
        self.chair_generator.leg_width = self.leg_width_dspnbx.value()

        self.chair_generator.cushion_width = self.cushion_width_dspnbx.value()
        self.chair_generator.cushion_depth = self.cushion_depth_dspnbx.value()
        self.chair_generator.cushion_thickness = self.cushion_height_dspnbx.value()

        self.chair_generator.create()
