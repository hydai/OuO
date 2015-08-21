"""
`jsonvalidator` is a simple validator for testing the format of json string
"""
import json
def jsonvalidator(jsonString):
    """
    Return the status of json validator
    """
    try:
        datas = json.loads(jsonString)
    except Exception as ex:
        print '| JSON | ERROR | ' + str(ex)
        return False

    return True
