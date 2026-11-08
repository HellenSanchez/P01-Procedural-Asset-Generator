import maya.cmds as cmds


class ChairGenerator():

    def __init__(self):
        # Seat parameters
        self.seat_width = 2.0
        self.seat_depth = 2.0
        self.seat_thickness = 0.2

        # Leg parameters
        self.leg_height = 2.0
        self.leg_width = 0.2

        # Seat apron parameters
        self.apron_height = 0.3
        self.apron_thickness = 0.15

    # Main function to create the chair
    def create(self):
        self.create_seat()
        self.create_legs()
        self.create_seat_apron()

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
    def create_legs(self):

        # Front left leg
        self.leg1, self.leg1_node = cmds.polyCube(
            name="leg1",
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
            name="leg2",
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

        # Back left leg
        self.leg3, self.leg3_node = cmds.polyCube(
            name="leg3",
            width=self.leg_width,
            height=self.leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg3}.translateY",
            -self.leg_height / 2.0
        )

        cmds.setAttr(
            f"{self.leg3}.translateX",
            -self.seat_width / 2.0 + self.leg_width / 2.0
        )

        cmds.setAttr(
            f"{self.leg3}.translateZ",
            -self.seat_depth / 2.0 + self.leg_width / 2.0
        )

        # Back right leg
        self.leg4, self.leg4_node = cmds.polyCube(
            name="leg4",
            width=self.leg_width,
            height=self.leg_height,
            depth=self.leg_width
        )

        cmds.setAttr(
            f"{self.leg4}.translateY",
            -self.leg_height / 2.0
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

    # Create seat cushion

    # Create backrest

    # Create backrest supports

    # Group all chair objects
