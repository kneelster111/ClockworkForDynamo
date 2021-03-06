import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *
from System.Collections.Generic import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
nestedcurves = IN[0]
revision = UnwrapElement(IN[1])
view = UnwrapElement(IN[2])
elementlist = list()

TransactionManager.Instance.EnsureInTransaction(doc)
for curves in nestedcurves:
	Curvelist = list()
	for curve in curves:
		Curvelist.append(curve.ToRevitType())
	icurves = List[Curve](Curvelist)
	revcloud = RevisionCloud.Create(doc, view, revision.Id, icurves);
	elementlist.append(revcloud)
TransactionManager.Instance.TransactionTaskDone()

OUT = elementlist