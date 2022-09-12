import sys
import os
import bpy

Space = bpy.data.texts["Space"].as_module()


def main() -> None:
    """Main function, initializes solver and creates cubes for 5 iterations of Conways game of life"""
    solver = Solver()
    x_offset_scale = 5
    for i in range(10):
        solver.realize(i * x_offset_scale)
        solver.update()


class Solver:
    """Instantiates a Space object with rules and dimensions for 3d cellular automata"""

    def __init__(self) -> None:
        self.RULESET = "B3/S23"
        self.Life = Space.Space(5, 5, 5, chance_1_divided_by=4)
        self.Life.set_rules(self.RULESET)
        self.Life.randomize()
        self.Life.update()
        self.state = self.Life.export()
        self.shape = self.state.shape

    def update(self):
        """Updates the state variable:
        - state is a 3D numpy array of shape (5,5,5) ) (can be changed)
        - calling this updates the array to the next generation"""
        self.Life.update()
        self.state = self.Life.export()

    def create_cube(self, pos: tuple, x_offset: int):
        """Creates a cube at the given point with an offset of x units from the centre.
        Inputs are:
        - pos : a tuple of (x,y,z) coordinates
        - x_offset : int value mentioning how many units to offset from the centre"""
        pos[1] += x_offset
        bpy.ops.mesh.primitive_cube_add(
            size=1, enter_editmode=False, align="WORLD", location=pos, scale=(1, 1, 1)
        )

    def realize(self, x_offset: int):
        """Creates cubes denoting live cells in the 3D cellular automata.
        - x_offset : int value mentioning how many units to offset from the centre"""
        xs = [x for x in range(self.shape[0])]
        ys = [x for x in range(self.shape[1])]
        zs = [x for x in range(self.shape[2])]
        for x in xs:
            for y in ys:
                for z in zs:
                    pos = [x, y, z]
                    if self.state[pos[0], pos[1], pos[2]] != 0:
                        print(f"created cube at, {pos}")
                        self.create_cube(pos, x_offset)


# call the main function
main()
