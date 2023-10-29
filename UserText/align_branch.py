__author__ = "ykish"
__version__ = "2023.10.30"
import System
import rhinoscriptsyntax as rs
import Grasshopper as gh

output_tree = gh.DataTree[System.Object]()
for y_path in y.Paths:
    print(y_path)
    x_value = x.Branch(y_path)[0]
    y_branch = y.Branch(y_path)
    y_branch_count =len(y_branch)
    print(x_value)
    for j in range(y_branch_count):
        output_tree.Add(x_value, y_path)

a = output_tree