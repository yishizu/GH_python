__author__ = "ykish"
__version__ = "2023.08.01"

import System
import rhinoscriptsyntax as rs
import ghpythonlib.treehelpers as th
import clr
clr.AddReference("Grasshopper")
import Grasshopper.Kernel.Data.GH_Path as ghpath
import Grasshopper.DataTree as datatree

output_tree = datatree[System.Object]()

for i in range(data0.BranchCount):
    branch_path = data0.Path(i)
    branch_values = data0.Branch(branch_path)
    
    if branch_path.Length>2:
        if data1.Paths[0].Length ==1:
            path = ghpath(branch_path[0])
            print(path)
            value = data1.Branch(path)[0]
            output_tree.Add(value, branch_path)
        elif data1.Paths[0].Length ==2:
            path1 = branch_path[0]
            path2 = branch_path[2]
            path = ghpath(path1, path2)
            #path = gh.Kernel.Data.GH_Path(0, 0)
            print( data1.ItemExists(path, 0))
            if data1.ItemExists(path, 0):
                value = data1.Branch(path)[0]
                output_tree.Add(value, branch_path)
                print(value)
            else:
                value = data1.Branch(branch_path)[0]
                output_tree.Add(value, branch_path)
    else:
        print( data0.Path(i)[0])
        branch_path = ghpath(data0.Path(i)[0])
        #branch_path = data0.Path(i)
        value = data1.Branch(branch_path)[0]
        output_tree.Add(value, data0.Path(i))


a =output_tree