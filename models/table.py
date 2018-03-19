from collections import OrderedDict
from models import Model, DynamicModel # Not sure which one I'll need yet.

class TableModel(Model):
    def __init__(this, tileRows, tileColumns):
        # Track the dimensions of the table.
        this.__tileRows = tileRows
        this.__tileColumns = tileColumns
        this.__evidenceFolders = OrderedDict()

    def getTileRows(this):
        return this.__tileRows

    def getTileColumns(this):
        return this.__tileColumns

    ## TODO: Add evidence folder model.
    def addEvidenceFolder(this, identifier, evidenceFolder):
        this.__evidenceFolders[identifier] = evidenceFolder

    def getEvidenceFolders(this):
        return this.__evidenceFolders

    def nixEvidenceFolder(this, identifier):
        evidenceFolder = None

        if identifier in this.__evidenceFolders:
            evidenceFolder = this.__evidenceFolders[identifier]

        return evidenceFolder
