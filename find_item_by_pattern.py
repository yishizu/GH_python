__author__ = "ykish"
__version__ = "2023.11.06"
import System
import clr
clr.AddReference("Grasshopper")
import Grasshopper.Kernel.Data.GH_Path as ghpath
import Grasshopper.DataTree as DataTree
clr.AddReference('System')
from System.Text.RegularExpressions import Regex


def find_item_with_pattern(tree, indices, keywords):
    output_tree = DataTree[object]()
    for i in range(tree.BranchCount):
        branch_path = tree.Path(i)
        value_list = tree.Branch(i)
        if not keywords:  # キーワードリストが空の場合
            if indices:  # インデックスリストが空でない場合
                first_index_value = value_list[indices[0] - 1] if indices[0] - 1 < len(value_list) else None
                if first_index_value is not None:
                    output_tree.Add(first_index_value, branch_path)
        else:
            for index in indices:
                # Ensure the index is within the bounds of the branch list
                if index - 1 < len(value_list):
                    value = value_list[index - 1]
                    for key in keywords:
                        # Escape the keyword to handle special regex characters
                        pattern = Regex("^{0}".format(Regex.Escape(key)))
                        if pattern.IsMatch(value):
                            if not "F" in value:
                                output_tree.Add(value, branch_path)
                                break  # マッチしたら他のキーワードはチェックしない
    return output_tree
    

a = find_item_with_pattern(_names, _indices, _keywords)