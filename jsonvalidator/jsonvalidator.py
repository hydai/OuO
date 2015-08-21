"""
`jsonvalidator` is a simple validator for testing the format of json string
"""
import json
def jsonvalidator(jsonString):
    """
    Return the status of json validator
    """
    isValid = True
    try:
        datas = json.loads(jsonString)
    except Exception as ex:
        isValid = False
        print '| JSON | ERROR | ' + str(ex)

    return isValid
