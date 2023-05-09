__author__ = "ykish"
__version__ = "2023.05.08"

import rhinoscriptsyntax as rs

import Rhino
import scriptcontext as sc

def get_usertext(guid):
    doc = Rhino.RhinoDoc.ActiveDoc
    rhino_object = doc.Objects.Find(guid)
    if rhino_object:
        mydict = rhino_object.Attributes.GetUserStrings()
        values =[]
        keys = mydict.AllKeys
        for k in keys:
            values.append(mydict[k])
        return keys, values
    else:
        return None

guid = curve # 入力パラメータとして追加したGuid

usertext_value = get_usertext(guid)[1]
usertext_key = get_usertext(guid)[0]