import sys
import os
import bpy
import numpy as np
import time
Space = bpy.data.texts["Space"].as_module()

def main() -> None:
#    RULESET: str = "B3/S23"
#    Life = Space.Space(5, 5, 4, chance_1_divided_by=4)
#    Life.set_rules(RULESET)
#    Life.randomize()
#    state = Life.export()
#    print(state.shape)
    mat = bpy.data.materials['Material.002']
    solver = Solver()
    print(solver.shape)
    for i in range(9):
        solver.realize()
        solver.update()
        select_metaballs()
        obj = mesh_metaballs()
        obj.material_slot_add()
#        obj.data.materials[0] = mat
    user_data = bpy.data.user_map()
    meshes = []
    for mesh in bpy.data.meshes.keys():
        mesh = bpy.data.meshes[mesh]
        if('Mesh' in mesh.name):
            if(len(user_data[mesh]) > 0):
                mesh.materials[0] = mat
                print(f"Changed mat for {mesh.name}")
                meshes.append(mesh)

class Solver():
    def __init__(self):
        self.RULESET = "B3/S23"
        self.Life = Space.Space(5, 5, 5, chance_1_divided_by=4)
        self.Life.set_rules(self.RULESET)
        self.Life.randomize()
        self.Life.update()
        self.state = self.Life.export()
        self.shape = self.state.shape
    def map_to_space(self,dims):
        pass
    def update(self):
        self.Life.update()
        self.state = self.Life.export()

    def create_ball(self,pos):
        bpy.ops.object.metaball_add(type='BALL', enter_editmode=False, align='WORLD', location=pos, scale=(1, 1, 1))

    def realize(self):
        xs = [x for x in range(self.shape[0])]
        ys = [x for x in range(self.shape[1])]
        zs = [x for x in range(self.shape[2])]
        for x in xs:
            for y in ys:
                for z in zs:
                    pos = [x,y,z]
                    if(self.state[pos[0],pos[1],pos[2]] != 0):
                        print(f"yes, {pos}")
                        self.create_ball(pos)

def select_metaballs():
    bpy.ops.object.select_grouped(type='TYPE')

def mesh_metaballs():
    bpy.ops.object.convert(target='MESH')
    return bpy.ops.object

def delete_mesh(object):
    object.delete()
    

main()