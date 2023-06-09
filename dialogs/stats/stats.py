from utils.intents import StatsIntents
from .config import getConfig
from utils.responseHelper import *
from utils.triggerHelper import *


def getResponse(event, allDialogs=None):
    config = getConfig(event)
    return createResponse(event, config)


def isTriggered(event):
    return isInCommandOr(event, StatsIntents) and isInLastContext(event, 'mainMenu')


stats = {"getResponse": getResponse, "isTriggered": isTriggered}
