import numpy as np
my_module = bpy.data.texts["my_module"].as_module()

def main() -> None:
    RULESET: str = "B3/S23"
    Life = Space(5, 5, 4, chance_1_divided_by=4)
    Life.set_rules(RULESET)
    Life.randomize()
    