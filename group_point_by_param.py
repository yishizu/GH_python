import rhinoscriptsyntax as rs
import Grasshopper as gh
import scriptcontext as sc
import System
import Rhino.Geometry as rg
import math
import ghpythonlib.treehelpers as th

def group_points_by_param(points, params, tolerance=0.001):
    grouped_points = {}
    
    for i, point in enumerate(points):
        p = params[i]
        key_found = None
        for key in grouped_points.keys():
            if abs(key - p) < tolerance:
                key_found = key
                break
        
        if key_found is not None:
            grouped_points[key_found].append(point)
        else:
            grouped_points[p] = [point]
            
    
    return grouped_points

input_tree_points = points
input_tree_params = params
output_tree = gh.DataTree[System.Object]()
for i in range(input_tree_points.BranchCount):
    print(i)
    branch_path = input_tree_points.Path(i)
    branch_values = input_tree_points.Branch(branch_path)
    branch_values2 = input_tree_params.Branch(branch_path)
    grouped_points = group_points_by_param(branch_values, branch_values2)
    sorted_keys = sorted(grouped_points.keys())
    for j, key in enumerate(sorted_keys):
        output_tree.AddRange(grouped_points[key], gh.Kernel.Data.GH_Path(i, j))
#grouped_points = group_points_by_param(points, params)
#sorted_keys = sorted(grouped_points.keys())
tree = output_tree