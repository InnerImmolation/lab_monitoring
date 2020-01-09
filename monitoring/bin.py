from monitoring.Export import Export


def start(interval, type):
    result = Export(interval, type)
    return result.exportResult()
