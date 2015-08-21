function isJSONValid(jsonString) {
    try {
        JSON.parse(jsonString);
    } catch (e) {
        return false;
    }
    return true;
}

function getJSONColumn(jsonString) {
    return Object.keys(JSON.parse(jsonString))
}
