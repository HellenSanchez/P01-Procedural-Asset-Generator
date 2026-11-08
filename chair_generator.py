import maya.cmds as cmds


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

    # Main function to create the chair
    def create(self):
        self.create_seat()
        self.create_legs()
        self.create_seat_apron()
        self.create_seat_cushion()
        self.create_backrest()

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
            self.seat_thickness / 2.0 + self.cushion_thickness / 2.0
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

    # Group all chair objects
