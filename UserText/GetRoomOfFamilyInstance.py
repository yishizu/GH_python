__author__ = "ykish"
__version__ = "2023.10.15"

import clr

# Revit APIアセンブリをインポート
clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
clr.AddReference('RhinoInside.Revit')
import RhinoInside.Revit as RIR
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, FamilyInstance,LocationPoint
from Autodesk.Revit.UI import TaskDialog



def get_room_of_instance(doc, instance):
    """
    Given a FamilyInstance, find the room it belongs to.
    """
    location = instance.Location
    if location and isinstance(location, LocationPoint):
        point = location.Point
        room = doc.GetRoomAtPoint(point)
        if room:
            return room
    return None

# インプットを設定
doc = RIR.Revit.ActiveUIDocument.Document
instance = familyInstances

room = get_room_of_instance(doc, instance)
if room:
    param = room.LookupParameter("名前")
    if param:
        roomNames = param.AsString()  # 文字列としてパラメータ値を取得
    else:
        roomNames = None

