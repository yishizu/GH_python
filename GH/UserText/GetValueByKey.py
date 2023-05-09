__author__ = "ykish"
__version__ = "2023.05.08"

        
import rhinoscriptsyntax as rs
import Rhino
        
rhdoc = Rhino.RhinoDoc.ActiveDoc
geometry = rhdoc.Objects.Find(id)
print geometry
my_dict = geometry.Attributes.GetUserStrings()
V = my_dict[key]