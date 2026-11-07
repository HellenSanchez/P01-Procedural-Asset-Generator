import maya.cmds as cmds


class ChairGenerator():

    def __init__(self):
        self.seat_width = 2.0
        self.seat_depth = 2.0
        self.seat_thickness = 0.2

    def create(self):
        self.create_seat()

    def create_seat(self):
        self.seat_obj, self.seat_node = cmds.polyCube(
            name="seat",
            width=self.seat_width,
            height=self.seat_thickness,
            depth=self.seat_depth
        )

        return self.seat_obj
    