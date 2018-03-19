## Tracks the paths of assets.
__assets = dict()

## Tracks the loaded assets (loading occurs when app calls loadAssets(...)).
__images = dict()
__audios = dict()

## For now, just assume 'config.ini' contains an [assets] record.
assetsRecordFound = False
with open("config.ini", "r") as configFile:
    for line in configFile:
        ## Strip the line ending.
        line = line.strip("\r\n")
        if not assetsRecordFound and line == "[assets]":
            assetsRecordFound = True
            ## GOTO the next line
            continue
        if assetsRecordFound:
            ## Allow finishing of reading the assets record early.
            if len(line) == 0:
                break

            ## Process the assette record fields.
            if line.startswith("image:"):
                ## Load the image key and path.
                parts = line.split(":")[1].split("=")
                key = parts[0]
                path = parts[1]
                del parts
                __assets[key] = ("image", path)

## Allows the application to specify the loader object that imports the discovered assets.
def loadAssets(loader, logger = None):
    for key, asset in __assets.iteritems():
        kind, path = asset
        if not logger is None:
            logger.debug(str.format("Asset: \"{0}\" ({1}) at \"{2}\"", key, kind, path))
        if kind == "image":
            __images[key] = loader.loadImage(path)
        elif kind == "audio":
            __audios[key] = loader.loadAudio(path)

def getImage(assetKey):
    if not assetKey in __images.keys():
        raise ValueError(str.format("Unknown image asset requested: {0}", assetKey))
    return __images[assetKey]

def getAudio(assetKey):
    if not assetKey in __audios.keys():
        raise ValueError(str.format("Unknown audio asset requested: {0}", assetKey))
    return __audios[assetKey]
