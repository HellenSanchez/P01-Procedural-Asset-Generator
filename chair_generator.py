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

    # Main function to create the chair
    def create(self):
        self.create_seat()
        self.create_legs()

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

    # Create wooden seat apron (frame underneath the seat)

    # Create seat cushion

    # Create backrest

    # Create backrest supports

    # Group all chair objects
    