"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""
__author__ = "ykish"
__version__ = "2023.11.06"
import System
import clr
clr.AddReference("Grasshopper")
import Grasshopper.Kernel.Data.GH_Path as ghpath
import Grasshopper.DataTree as datatree
clr.AddReference('System')
from System.Text.RegularExpressions import Regex

for i in range(_names.BranchCount):
    value_list = _names.Branch(i)
    for index in _indices:
        value = value_list[index-1]
        for key in _keywords:
            print(key)
            pattern = Regex("^{0}".format(key))
            if pattern.IsMatch(value):
                print(value)
            else:
                print("")

def find_item_with_pattern(tree, indices, keywords):
    output_tree = datatree[System.Object]()
    for i in range(tree.BranchCount):
        branch_path = tree.Path(i)
        value_list = tree.Branch(i)
        for index in indices:
            value = value_list[index-1]
            for key in keywords:
                pattern = Regex("^{0}".format(key))
                if pattern.IsMatch(value):
                    output_tree.Add(value, branch_path)
    return output_tree
    

a = find_item_with_pattern(_names, _indices, _keywords)