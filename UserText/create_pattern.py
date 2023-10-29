import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from Autodesk.Revit.ApplicationServices import Application
from System import Enum
from RhinoInside.Revit import Revit

def main(Form, Trigger, U, V, Pattern):
    if Form is None:
        return

    doc = Revit.ActiveDBDocument

    try:
        form = Form
        freeform = Form
    except Exception as txnErr:
        print(txnErr.Message)

    thisDsList = []

    if Trigger:
        transaction = Transaction(doc, "CSharpWall")
        transaction.Start()

        try:
            options = transaction.GetFailureHandlingOptions()
            options = options.SetDelayedMiniWarnings(True)
            options = options.SetForcedModalHandling(True)

            if form:
                thisDsList = DivideSurface(doc, form, U, V, Pattern)
            else:
                thisDsList = DivideSurface(doc, freeform, U, V, Pattern)

            a = thisDsList
            transaction.Commit(options)

        except Exception as txnErr:
            print(txnErr.Message)
            transaction.RollBack()

    return thisDsList

def DivideSurface(document, form, u, v, name):
    dsList = []
    application = document.Application
    opt = application.Create.NewGeometryOptions()
    opt.ComputeReferences = True

    geomElem = form.get_Geometry(opt)
    for geomObj in geomElem:
        solid = geomObj
        for face in solid.Faces:
            faceRef = face.Reference
            if faceRef:
                divSrf = DividedSurface.GetDividedSurfaceForReference(document, faceRef)
                if divSrf is None:
                    print("Null")
                    divSrf = DividedSurface.Create(document, face.Reference)

                divSrf.ChangeTypeId(TilePatternIdByName(document, name))
                srU = divSrf.USpacingRule
                srU.SetLayoutFixedNumber(u, SpacingRuleJustification.Center, 0, 0)

                srV = divSrf.VSpacingRule
                srV.SetLayoutFixedNumber(v, SpacingRuleJustification.Center, 0, 0)

                dsList.append(divSrf)
                break

    return dsList

def TilePatternIdByName(document, name):
    tilePatterns = document.Settings.TilePatterns
    pattern = Enum.Parse(TilePatternsBuiltIn, name)
    tilePattern = tilePatterns.GetTilePattern(pattern)

    return tilePattern.Id

# Example usage:
result = main(form, trigger, u, v, pattern)
