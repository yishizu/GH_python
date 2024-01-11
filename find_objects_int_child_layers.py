__author__ = "ykish"
__version__ = "2023.12.26"
import System
import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
import clr
clr.AddReference("Grasshopper")
import Grasshopper.Kernel.Data.GH_Path as ghpath
import Grasshopper.DataTree as datatree

def find_objects_in_child_layers(parent_layer):
    output_tree = datatree[System.Object]()
    original_doc = sc.doc
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    z_offsets = datatree[System.Object]()
    x_offsets = datatree[System.Object]()
    diameters = datatree[System.Object]()
    spacing = datatree[System.Object]()
    names = datatree[System.Object]()
    child_layers = rs.LayerChildren(parent_layer)
    
    if not child_layers:
        return objects

    # 各子レイヤーを走査
    for i, layer in enumerate(child_layers):
        # レイヤー名に指定された文字列が含まれている場合
        levels = layer.Split(':')[-1]
        print(levels)
        levels = levels.Split('_')
        layer_objects = rs.ObjectsByLayer(layer)
        for j,level in enumerate(levels):
            print(level)
            
            
            if layer_objects:
                
                branch_path = ghpath(i,j)
                output_tree.AddRange(layer_objects, branch_path)
                for k,d in enumerate(dict):
                    if level in d['name']:
                        print(d['z_offset'])
                        z_offsets.Add(d['z_offset'], branch_path)
                        x_offsets.Add(d['x_offset'], branch_path)
                        diameters.Add(d['diameter'], branch_path)
                        spacing.Add(d['spacing'], branch_path)
                        names.Add(d['name'], branch_path)
                        names.Add(dict[k-1]['name'], branch_path)
    sc.doc = original_doc
    return output_tree, z_offsets, names, x_offsets, diameters, spacing

result_objects, z_offsets, names, x_offsets, diameters, spacing = find_objects_in_child_layers(parent_layer)
