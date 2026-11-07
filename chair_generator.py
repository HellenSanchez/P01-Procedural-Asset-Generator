import maya.cmds as cmds


class ChairGenerator():

    def __init__(self):
        # Seat parameters
        self.seat_width = 2.0
        self.seat_depth = 2.0
        self.seat_thickness = 0.2

    # Main function to create the chair
    def create(self):
        self.create_seat()

    # Create seat
    def create_seat(self):
        self.seat_obj, self.seat_node = cmds.polyCube(
            name="seat",
            width=self.seat_width,
            height=self.seat_thickness,
            depth=self.seat_depth
        )

        return self.seat_obj

    # Create four chair legs

    # Create wooden seat apron (frame underneath the seat)

    # Create seat cushion

    # Create backrest

    # Create backrest supports

    # Group all chair objects
    