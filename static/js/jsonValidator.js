function isJSONValid(jsonString) {
    try {
        JSON.parse(jsonString);
    } catch (e) {
        return false;
    }
    return true;
}
