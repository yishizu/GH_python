import rhinoscriptsyntax as rs

import clr
clr.AddReference('System.Core')
clr.AddReference('RhinoInside.Revit')
clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI')
import math
import Rhino
import RhinoInside
import Grasshopper
import ghpythonlib.treehelpers as th
import Grasshopper.Kernel.Data.GH_Path as GH_Path
import Grasshopper.DataTree as DataTree
import scriptcontext
from RhinoInside.Revit import Revit, Convert
from Autodesk.Revit import DB
from Autodesk.Revit.DB.Structure import *
from System.Collections.Generic import List, IList
from System import Enum, Action

doc = Revit.ActiveDBDocument
if host is not None:
    # Get all rebars in the host
    allRebars  = DB.FilteredElementCollector(doc).OfClass(DB.Structure.Rebar).ToElements()
    slabRebars = [rebar for rebar in allRebars if rebar.GetHostId() == host.Id]
    markRebars = [rebar for rebar in slabRebars if rebar.get_Parameter(DB.BuiltInParameter.ALL_MODEL_MARK).AsString() == mark]
    shapeRebars = [rebar for rebar in slabRebars if rebar.get_Parameter(DB.BuiltInParameter.REBAR_SHAPE).AsValueString() == shapeName]

for rebar in allRebars:
    shape = rebar.get_Parameter(DB.BuiltInParameter.REBAR_SHAPE)
    print(shape.AsValueString())