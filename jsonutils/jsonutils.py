"""
`jsonutils` is a tool kit for testing json property.
"""
import json
def jsonvalidator(jsonString):
    """
    `jsonutils` is a simple validator for testing the format of json string

    Return:
        True
            Valid
        False
            Invalid
    """
    try:
        datas = json.loads(jsonString)
    except Exception as ex:
        print '| JSON | ERROR | ' + str(ex)
        return False

    return True

def jsoncolumns(jsonString):
    """
    Return a list of columns' name.

    Return:
        list
            A list of columns' name.
        None
            There is no column or the input json string is invalid.
    """
    if jsonvalidator(jsonString):
        return json.loads(jsonString).keys()
    else:
        return []
