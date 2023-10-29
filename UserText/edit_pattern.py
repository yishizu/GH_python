

import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System import Enum
from RhinoInside.Revit import Revit
from System.Collections.Generic import List

def main(FormId, Trigger, U, V, Pattern):
    if FormId == -1:
        return

    doc = Revit.ActiveDBDocument
    collector = List[Element](FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_MassForm).ToElements())
    element = None

    for thisform in collector:
        if thisform.Id.IntegerValue == FormId:
            element = doc.GetElement(thisform.Id)
            break

    thisDsList = []

    if Trigger and element:
        transaction = Transaction(doc, "CSharpWall")
        transaction.Start()

        try:
            options = transaction.GetFailureHandlingOptions()
            options = options.SetDelayedMiniWarnings(True)
            options = options.SetForcedModalHandling(True)

            doc.Regenerate()
            thisDsList = DivideSurface(doc, element, U, V, Pattern)
            
            transaction.Commit(options)
        except Exception as txnErr:
            print(txnErr.Message)
            transaction.RollBack()

    return thisDsList

def DivideSurface(document, element, u, v, name):
    dsList = []

    for faceRef in DividedSurface.GetReferencesWithDividedSurfaces(element):
        divSrf = DividedSurface.GetDividedSurfaceForReference(document, faceRef)

        divSrf.ChangeTypeId(TilePatternIdByName(document, name))

        srU = divSrf.USpacingRule
        srU.SetLayoutFixedNumber(u, SpacingRuleJustification.Center, 0, 0)

        srV = divSrf.VSpacingRule
        srV.SetLayoutFixedNumber(v, SpacingRuleJustification.Center, 0, 0)

    return dsList

def TilePatternIdByName(document, name):
    tilePatterns = document.Settings.TilePatterns
    pattern = Enum.Parse(TilePatternsBuiltIn, name)
    tilePattern = tilePatterns.GetTilePattern(pattern)

    return tilePattern.Id

# Example usage:
result = main(formId, trigger, u, v, pattern)
